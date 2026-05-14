# 📘 Day 16: Re-ranking in RAG

---

## 🧠 What is Re-ranking?

Re-ranking means re-evaluating retrieved chunks and sorting them again based on deeper semantic relevance.

👉 It improves retrieval quality after vector search.

---

## 🔥 Why is Re-ranking Needed?

Vector search is:

* fast
* scalable

But:

* sometimes inaccurate
* may retrieve noisy or weakly relevant chunks

👉 Re-ranking improves accuracy.

---

# 🔁 Retrieval + Re-ranking Pipeline

Query
→ Vector Search
→ Top-K Chunks Retrieved
→ Re-ranker
→ Best Relevant Chunks
→ LLM
→ Final Answer

---

# 🔹 Step 1: Initial Retrieval

Vector search retrieves top-k chunks using embeddings and similarity search.

Example:

```python id="j8d7vs"
top_k = 10
```

---

# 🔹 Step 2: Re-ranking

A re-ranker re-evaluates retrieved chunks using deeper semantic understanding and reorders them based on relevance.

---

## 🎯 Core Idea

Vector search focuses on:

* speed

Re-ranking focuses on:

* accuracy

---

# ⚠️ Problems with Vector Search

---

## ❌ Surface Similarity

Query:
"python for AI"

Retrieved:

* python snake ❌
* python programming ✔

---

## ❌ Ambiguous Words

Examples:

* bank
* apple
* java

---

## ❌ Noisy Retrieval

Weakly relevant chunks may appear in top-k results.

---

# 🔥 How Re-ranking Works

Instead of only comparing vectors, re-rankers analyze:

* query
* chunk

together.

👉 This enables deeper semantic understanding.

---

# 🔥 Cross-Encoder (Very Important)

Most modern re-rankers use Cross-Encoder models.

---

## 🔹 Embedding Model

Embedding models:

* encode query separately
* encode chunks separately
* compare vectors

✔ Fast
❌ Less accurate

---

## 🔹 Cross-Encoder

Cross-Encoder processes:

* query + chunk together

Example:

Query:
"What is AI?"

Chunk:
"AI uses neural networks."

👉 Better understanding of actual relevance.

---

# ⚠️ Tradeoff

| Embedding Search | Re-ranking    |
| ---------------- | ------------- |
| Fast             | Slower        |
| Scalable         | Expensive     |
| Approximate      | More accurate |

---

# 🔥 Why Not Re-rank All Chunks?

Suppose:

* millions of chunks exist

👉 Cross-encoder models are computationally expensive.

So modern systems:

1. use vector search to narrow candidates
2. rerank only top retrieved chunks

---

# 🔥 Impact of Re-ranking

Re-ranking improves:

* precision
* relevance
* faithfulness
* groundedness

👉 Helps reduce hallucination.

---

# 🔥 Better Context = Better Answers

Better retrieved chunks:
→ better context
→ more grounded responses
→ fewer hallucinations

---

# 🔥 Real-world Applications

* enterprise search
* legal assistants
* medical AI systems
* research copilots
* customer support bots

---

# 🔥 Common Re-ranking Models

Examples:

* BGE reranker
* Cohere rerank
* Cross-Encoder models

---

# 🎯 Key Takeaways

* Re-ranking improves retrieval accuracy
* Vector search retrieves candidates quickly
* Re-rankers reorder chunks using deeper understanding
* Cross-encoders provide better semantic relevance
* Modern RAG systems combine vector search + reranking

---

## 💡 My Understanding

Re-ranking improves retrieval quality by re-evaluating retrieved chunks using deeper semantic analysis and selecting the most relevant context for the LLM.

---
