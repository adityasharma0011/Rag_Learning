# Goal
# 👉 Query → embeddings
# 👉 Docs → embeddings
# 👉 similarity → best match

# 👉Vector search = finding nearest meaning using embeddings
# 👉“I implemented a semantic search system using embeddings and 
#   cosine similarity to retrieve top-k relevant documents.”


# step 1: Model Load-------------------------------------------------
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# step 2 : data
docs = [
    "Machine learning is a part of AI",
    "Deep learning uses neural networks",
    "Cricket is a popular sport",
    "Cooking is fun and creative"
]


# step 3: model load------------------------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')



# step 4 : doc embedding---------------------------------------------
doc_embeddings = model.encode(docs)


# step 5:  query input------------------------------------------------

query = ["i want to learn ai"]
query_embedding = model.encode(query) 


# step 6: similarity check-----------------------------------------------

similarity = cosine_similarity(query_embedding, doc_embeddings)
print(similarity)


# step 7: best match find-------------------------------------------------

best_index = np.argmax(similarity)
print("Best match:", docs[best_index])


# step 8: top k results find-------------------------------------------------
# sirf 1 nahi, top 2–3 docs chahiye----  RAG me:
# top 1 nahi
# top K chunks use hote hain

top_k = 2
indices = np.argsort(similarity[0])[-top_k:][::-1]
for i in indices:
    print(docs[i])



# step 9 : turning into function-------------------------------------------------

doc_embeddings = model.encode(docs)

def search(query, doc_embeddings, docs, model, top_k=2):
    query_embedding = model.encode([query])
    similarity = cosine_similarity(query_embedding, doc_embeddings)

    indices = np.argsort(similarity[0])[-top_k:][::-1]
    return [docs[i] for i in indices]

results = search("learn AI", doc_embeddings, docs, model)

for r in results:
    print(r)