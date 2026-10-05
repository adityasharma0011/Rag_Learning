import os
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import gradio as gr


# ---------------------------------------------------------------------------
# Setup: API key, chat model, embedding model
# ---------------------------------------------------------------------------

# Load the API key from a .env file in this folder, e.g:
# GROQ_API_KEY=gsk_...
# Get a free key at https://console.groq.com
load_dotenv(override=True)
groq_api_key = os.getenv("GROQ_API_KEY")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:8]}")
else:
    print("Groq API Key not set")


llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    temperature=0.3,
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_api_key,
)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

KNOWLEDGE_BASE_DIR = "knowledge_base"


# ---------------------------------------------------------------------------
# Step 1: Load every .md file from the knowledge base folder
# ---------------------------------------------------------------------------
# DirectoryLoader walks knowledge_base/ (including every subfolder, thanks
# to the "**/" glob) and loads each .md file into a Document. The subfolder
# + filename are kept in metadata["source"], so you always know which file
# an answer came from.

loader = DirectoryLoader(
    KNOWLEDGE_BASE_DIR,
    glob="**/*.md",
    loader_cls=TextLoader,
    show_progress=True,
)

documents = loader.load()
print(f"Loaded {len(documents)} documents from '{KNOWLEDGE_BASE_DIR}'")
for doc in documents:
    print(" -", doc.metadata["source"])


# ---------------------------------------------------------------------------
# Step 2: Split into chunks
# ---------------------------------------------------------------------------
# Files here are short, but splitting is good practice once files get
# longer (policies, guides, articles). RecursiveCharacterTextSplitter keeps
# each chunk a manageable size while preserving metadata["source"] on every
# chunk.

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

print(f"Split into {len(chunks)} chunks")


# ---------------------------------------------------------------------------
# Step 3: Embed the chunks and build a vector store
# ---------------------------------------------------------------------------
# Embeddings are generated locally with a free Hugging Face model
# (sentence-transformers/all-MiniLM-L6-v2) — no API key, no per-call cost.
# Only the chat model (llm) still uses the OpenAI-compatible API.

vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Quick manual test of retrieval
found = retriever.invoke("how long do I have to return something?")
for doc in found:
    print(doc.metadata["source"], "->", doc.page_content[:80].replace("\n", " "))


# ---------------------------------------------------------------------------
# Step 4: A small LCEL chain with a custom prompt
# ---------------------------------------------------------------------------
# Instead of RetrievalQA (which lives in the separate, sometimes-out-of-sync
# "langchain" package), this builds the same "retrieve, then ask the LLM"
# logic directly with LangChain Expression Language (LCEL), using only
# langchain-core — the same lightweight package that langchain-openai and
# langchain-community already depend on. That sidesteps the
# "ModuleNotFoundError: No module named 'langchain.chains'" error you can
# get if the full langchain package isn't installed in your environment.
#
# It still grounds the assistant in whatever was retrieved from the folder,
# and tells it to admit when the knowledge base does not cover something
# rather than guessing.

prompt_template = """You are an IT Support Knowledge Assistant.

Answer the user's question using ONLY the information provided in the
retrieved IT knowledge base.

Give clear, practical troubleshooting steps when the knowledge base
contains the required information.

If the knowledge base does not contain enough information to answer the
question, clearly say that you do not have enough information and
recommend contacting IT support.

Do not guess or invent troubleshooting steps.

IT Knowledge Base:
{context}

User question: {question}

Answer:"""

qa_prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)


def format_docs(docs):
    """Join retrieved documents' text into a single context string."""
    return "\n\n".join(doc.page_content for doc in docs)


# A small LCEL chain: retrieve -> fill the prompt -> call the LLM -> get
# plain text back. Only needs langchain-core, so it avoids the separate
# "langchain" package entirely.
qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | qa_prompt
    | llm
    | StrOutputParser()
)


# ---------------------------------------------------------------------------
# Step 5: A plain (non-streaming) response function
# ---------------------------------------------------------------------------

def answer_question(message, history=None):
    """Answer a customer's question using the RAG chain (no streaming)."""
    return qa_chain.invoke(message)


# Quick manual test
print(answer_question("Do you price match other stores?"))


# ---------------------------------------------------------------------------
# Step 6: The Gradio UI
# ---------------------------------------------------------------------------

message_input = gr.Textbox(
    label="Ask IT Support:",
    placeholder="Describe your IT problem...",
    lines=3
)
message_output = gr.Markdown(label="Answer:")

view = gr.Interface(
    fn=answer_question,
    title="AI Technical Support Assistant ",
    inputs=[message_input],
    outputs=[message_output],
    examples=[
    "My laptop is connected to Wi-Fi but I cannot access the internet.",
    "How do I reset my password?",
    "My VPN is not connecting.",
    "How can I troubleshoot a printer that is not printing?",
    "Outlook is not receiving emails. What should I do?",
    ],
    flagging_mode="never",
)

if __name__ == "__main__":
    view.launch(inbrowser=True)