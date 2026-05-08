# 🧠 Goal
# 👉 Large text → chunks
# 👉 chunks → embeddings
# 👉 query → best chunk retrieve

# 👉 💥 real RAG pipeline (without LLM)


text = """
Artificial Intelligence (AI) is a field of computer science.
Machine learning is a subset of AI that focuses on data-driven learning.
Deep learning is a type of machine learning using neural networks.
AI is used in healthcare, finance, and many industries.
"""


# step 2: basic chunking-------------------------------------------------

# def chunk_text(text, chunk_size=100):
#     chunks = []
#     for i in range(0, len(text), chunk_size):
#         chunks.append(text[i:i+chunk_size])
#     return chunks

# chunks = chunk_text(text)

# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i}:", chunk)
#  this is fix size chunking. problem- sentence can cut here.



# step 3: better chunking-------------------------------------------------

# better chunking - sentence based chunking. problem- sentence can be too long.

# chunks = text.split(". ")
# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i}:", chunk)

# step 8 : add overlap in chunking-------------------------------------------------
# ✔ context better preserve hoga
def chunk_with_overlap(text, chunk_size=100, overlap=10):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])
    return chunks

chunks = chunk_with_overlap(text, chunk_size=100, overlap=10)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}:", chunks[i])

# step 4: embedding on chunks-------------------------------------------------

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

chunk_embeddings = model.encode(chunks)




# step 5 : query search on chunks-------------------------------------------------

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

query = "lets play football"

query_embedding = model.encode([query])

similarity = cosine_similarity(query_embedding, chunk_embeddings)

print(similarity)




# step 6: chunk retrieval-------------------------------------------------
best_index = np.argmax(similarity)

print("Best chunk:", chunks[best_index])



# step 7 : top k chunnks retrieval-------------------------------------------------

top_k = 2
indices = np.argsort(similarity[0])[-top_k:][::-1]
for i in indices:
    print("Relevant chunk:", chunks[i])



