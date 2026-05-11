# 🔥 MOST IMPORTANT REALIZATION

# LlamaIndex koi magic nahi hai.
# Internally still:
                # chunking
                # embeddings
                # retrieval
                # context injection
# Framework bas automation deta hai.


# step 1 : install liberraries -----------------------------------------------------------------
# pip install llama-index llama-index-llms-ollama
# 🧠 WHY?
# llama-index--RAG framework.



# step 2: import libraries -----------------------------------------------------------------

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Local embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# SimpleDirectoryReader--->Documents read karega
# VectorStoreIndex-------->Embeddings + retrieval automatically manage karega
# Ollama------------------>Local LLM connect karega.
# by default ollama uses openai embeddings but i dont have api key so i am using local embedding model from huggingface.
# HuggingFaceEmbedding--->Embeddings generate karega using local huggingface model.




# step 3: load documents -----------------------------------------------------------------

document = SimpleDirectoryReader(input_files=["day10-11-12-Practical_part/data.txt"]).load_data()
# this can read txt-pdf-docs automatically.




# step 4: setup local llm ------------------------------------------------------------------

llm = Ollama(model="tinyllama")
# local llm ko connect karte hain.
# Ab LlamaIndex :  TinyLlama ko response generation ke liye use karega.




# step 5: create index -----------------------------------------------------------------

index = VectorStoreIndex.from_documents(documents=document, llm=llm)

# YAHI internally karta hai: documents → chunking → embeddings → vector store



# step 6 : create query engine -----------------------------------------------------------------

query_engine = index.as_query_engine(llm=llm)

# Ye internally manage karega:
# query
# → embedding
# → retrieval
# → prompt injection
# → llm response



# step 7: ask question -----------------------------------------------------------------

query = input("ask question : ")



# step 8 : query the rag system -----------------------------------------------------------------

response = query_engine.query(query)



# step 9 : print response -----------------------------------------------------------------

print("\n--- answer ---")
print(response)