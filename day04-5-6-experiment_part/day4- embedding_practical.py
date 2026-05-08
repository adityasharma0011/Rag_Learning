# Embedding = meaning match, not keyword match
# “Embeddings depend heavily on context — vague queries lead to ambiguous results.”


from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

# sentences = [
#     "I love machine learning",
#     "I enjoy studying AI",
#     "I hate rain",
#     "Football is fun"
# ]
# embeddings = model.encode(sentences)
# print(embeddings.shape)

docs = [
    "Machine learning is a part of AI",
    "Deep learning uses neural networks",
    "Cricket is a popular sport",
    "Cooking is fun"
]

doc_embeddings = model.encode(docs)

print(doc_embeddings.shape)






# Step 2: Similarity Check--------------------------------------------------------------------

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(doc_embeddings)

print(similarity)

# “This matrix shows how similar each sentence is to every other sentence using cosine similarity.”
# sentence 1 & 2 → high similarity ✔
# sentence  3 & 4 → low ❌




# Step 3: Real Query Matching--------------------------------------------------------------------

# query = ["I want to study deep learning"]
query = ["How to cook food"]

query_embedding = model.encode(query)

similarity = cosine_similarity(query_embedding, doc_embeddings)

print(similarity)

# 📊 Quick scale (yaad rakh)
# Score         	Meaning
# 0.8+	            very similar
# 0.5+	            related
# 0.2–0.4       	weak
# <0.2	            unrelated



#  Step 4: Best Match Find-------------------------------------------------

import numpy as np

best_index = np.argmax(similarity)

print("Best match:", docs[best_index])




# Step 7: Keyword vs Embedding Test-------------------------------------------------

docs = [
    "earn money fast",
    "get rich quick",
    "football match today"
]
query = ["make money quickly"]

# ✔ keyword match nahi
# ✔ embedding match karega



# ⚠️ Step 9: Limitations test-------------------------------------------------

# query = ["bank"]

# 👉 Docs:
# river bank
# money bank

# 👉 Observe:
# → confusion 😵

# output--------------------------------------------
# river bank  → 0.76  
# money bank  → 0.89  🔥 (highest)

# reason--------------------------------------------
# Embedding model kya karta hai?
# 👉 Wo dekhta hai:
# common usage / training data
# “bank” mostly financial context me use hota hai ,that's why --money bank → higher similarity
