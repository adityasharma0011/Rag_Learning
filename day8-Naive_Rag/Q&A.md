# 📘 Day 8: Naive RAG – Important Q&A

---

## ❓ 1. What is Naive RAG?

Naive RAG is a basic RAG pipeline that combines retrieval and generation by retrieving relevant chunks using embeddings and vector search, then passing those chunks as context to the LLM for answer generation.

---

## ❓ 2. What is the role of the Retriever?

The retriever retrieves relevant chunks using:

* chunking
* embeddings
* vector search

---

## ❓ 3. What is the role of the Generator?

The generator (LLM) uses the retrieved context and user query to generate the final answer.

---

## ❓ 4. Why is Chunking important in RAG?

Chunking improves retrieval quality by splitting large documents into smaller meaningful parts.

---

## ❓ 5. Why does Retrieval Quality matter?

The LLM depends on retrieved chunks for generating answers, so better retrieval leads to more accurate and meaningful responses.

---

## ❓ 6. How does RAG reduce hallucination?

RAG reduces hallucination by providing relevant external context to the LLM instead of forcing it to rely only on internal memory.

---

## ❓ 7. What is the difference between Retriever and Generator?

| Retriever              | Generator              |
| ---------------------- | ---------------------- |
| Finds relevant chunks  | Generates final answer |
| Uses embeddings/search | Uses LLM               |
| Handles retrieval      | Handles generation     |

---

## ❓ 8. What is a Vector Store?

A vector store stores embeddings for efficient similarity search.

Examples:

* FAISS
* Pinecone
* ChromaDB

---

## 🎯 Summary

* Naive RAG = Retrieve + Generate
* Retriever finds relevant context
* Generator creates final response
* Better retrieval improves answer quality

---
