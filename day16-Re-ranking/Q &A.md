# 📘 Day 16: Re-ranking – Important Q&A

---

## ❓ 1. What is Re-ranking in RAG?

Re-ranking is the process of re-evaluating retrieved chunks and sorting them again based on deeper semantic relevance.

---

## ❓ 2. Why is Re-ranking needed?

Vector search is fast but may retrieve noisy or weakly relevant chunks. Re-ranking improves retrieval accuracy.

---

## ❓ 3. What are the limitations of Vector Search?

Vector search may suffer from:

* surface similarity
* ambiguity
* noisy retrieval
* approximate matching

---

## ❓ 4. What is the difference between Embedding Search and Re-ranking?

| Embedding Search       | Re-ranking                    |
| ---------------------- | ----------------------------- |
| Fast                   | Slower                        |
| Approximate retrieval  | More accurate retrieval       |
| Uses vector similarity | Uses deeper semantic analysis |

---

## ❓ 5. What is a Cross-Encoder?

A Cross-Encoder processes the query and chunk together to better understand semantic relevance.

---

## ❓ 6. Why not Re-rank all chunks?

Re-ranking all chunks is computationally expensive and slow for large datasets.

---

## ❓ 7. How does Re-ranking reduce hallucination?

Re-ranking improves context quality, which helps the LLM generate more grounded and accurate responses.

---

## ❓ 8. What metrics improve with Re-ranking?

Re-ranking improves:

* precision
* relevance
* faithfulness
* groundedness

---

## ❓ 9. What is the standard modern RAG pipeline?

Query
→ Vector Search
→ Top-K Retrieval
→ Re-ranking
→ LLM

---

## ❓ 10. What is the main tradeoff in Re-ranking?

The main tradeoff is:

* higher accuracy
  vs
* slower retrieval speed

---

## 🎯 Summary

* Vector search retrieves candidates quickly
* Re-ranking improves retrieval quality
* Cross-encoders provide deeper semantic understanding
* Better retrieval leads to better RAG responses

---
