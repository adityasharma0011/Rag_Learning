# 📘 Day 8: Naive RAG

---

## 🧠 What is RAG?

RAG stands for **Retrieval-Augmented Generation**.

It is a system that:

1. Retrieves relevant information
2. Uses an LLM to generate the final answer

---

## 🔥 Core Idea

Instead of relying only on the LLM’s internal knowledge, RAG retrieves external relevant data and provides it as context.

👉 Retrieve first → Generate later

---

## 🧠 What is Naive RAG?

Naive RAG is the simplest form of a RAG pipeline without advanced optimizations like:

* reranking
* evaluation
* hybrid search
* advanced retrieval

It mainly follows:
Retrieve → Generate

---

## 🔁 Naive RAG Pipeline

Documents
→ Chunking
→ Embeddings
→ Vector Store
→ User Query
→ Query Embedding
→ Similarity Search
→ Retrieve Relevant Chunks
→ Prompt + Context
→ LLM
→ Final Answer

---

## ⚙️ Step-by-step Flow

### 🔹 1. Documents

Input knowledge source:

* PDFs
* Notes
* Websites
* Text files

---

### 🔹 2. Chunking

Large documents are split into smaller meaningful chunks.

👉 Improves retrieval quality
👉 Handles token limits

---

### 🔹 3. Embeddings

Chunks are converted into vectors.

👉 Similar meaning → similar vectors

---

### 🔹 4. Vector Store

All embeddings are stored for retrieval.

Examples:

* FAISS
* Pinecone
* ChromaDB

---

### 🔹 5. Query Embedding

User query is also converted into a vector.

---

### 🔹 6. Similarity Search

The system compares:

* query embedding
* chunk embeddings

👉 Retrieves top relevant chunks

---

### 🔹 7. Prompt Construction

Retrieved chunks are added as context in the prompt.

Example:

Context:
{retrieved chunks}

Question:
{user query}

---

### 🔹 8. LLM Generation

The LLM uses:

* user query
* retrieved context

to generate the final response.

---

## 🎯 Retriever vs Generator

| Component       | Role                   |
| --------------- | ---------------------- |
| Retriever       | Finds relevant chunks  |
| Generator (LLM) | Generates final answer |

---

## 🔥 Why RAG is Powerful

* Uses external knowledge
* Reduces hallucination
* Supports private/custom data
* Provides more accurate responses

---

## ⚠️ Limitations of Naive RAG

* Bad chunking → poor retrieval
* Weak embeddings → wrong context
* No reranking
* Limited context window

---

## 🧠 Important Insight

👉 Retrieval quality directly affects answer quality.

Better Retrieval → Better Context → Better Answers

---

## 🎯 Key Takeaways

* Naive RAG combines retrieval and generation
* Retrieval uses embeddings and vector search
* LLM generates answers using retrieved context
* RAG reduces hallucination by grounding responses in retrieved data

---

## 💡 My Understanding

Naive RAG retrieves relevant chunks using embeddings and vector search, then passes those chunks as context to an LLM for accurate answer generation.

---
