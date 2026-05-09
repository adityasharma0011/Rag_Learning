from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import ollama

#  step 1: Initialize embedding model -----------------------------------------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')



# step 2: Read documents-------------------------------------------------------------------
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data.txt")

with open(file_path, "r") as file:
    documents = file.readlines()



# step 3: Create document embeddings-------------------------------------------------------------------
doc_embeddings = model.encode(documents)



# step 4: User query--------------------------------------------------------------------------------
query = input("ask question : ")

# Query embedding
query_embedding = model.encode([query])

# Similarity search
similarities = cosine_similarity(query_embedding, doc_embeddings)

# Best match
top_k = 3

top_indices = np.argsort(similarities[0])[-top_k:]

retrieved_chunks = [documents[i] for i in top_indices]

retrieved_text = "\n".join(retrieved_chunks)


# Single best chunk risky hota hai.
# Isliye:
# production RAG systems:
                            # top-k retrieval
                            # reranking
                            # hybrid search
                            # use karte hain.




# step 5: Show retrieved chunk-----------------------------------------------------------------------
print("\nRetrieved Context:")
print(retrieved_text)




# step 6: Final prompt--------------------------------------------------------------------------------
prompt = f"""

You are a helpful AI assistant.

Answer ONLY from the provided context.
If answer is not present in context, say:
"I don't know from the given context."


Context:
{retrieved_text}

Question:
{query}
"""

# LLM response
response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

# Final answer
print("\nFinal Answer:")
print(response['message']['content'])




# final obseervations : herre i am using a small llama model,so response quitely is not that good, but with better model ans will be better.
#                     : embedding model is also small, so retreival is not that good
#                    : but overall process is working fine, and i am able to get answer from the context.
#                    : i have succesfully implemented naive rag system and understood the process,structure and flow of the system....