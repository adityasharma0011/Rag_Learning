# 🚀 RAG Learning Journey

This repository contains my step-by-step learning and implementation journey of Retrieval Augmented Generation (RAG) systems.

The goal of this journey is not only to use RAG tools, but to deeply understand how modern AI retrieval systems work internally.

---

# 📚 What I Learned So Far

## ✅ Day 1 — Embeddings

Learned:
- text embeddings
- vector representation
- semantic meaning
- cosine similarity

Implemented:
- converting text into vectors
- similarity comparison between sentences

---

## ✅ Day 2 — Vector Search

Learned:
- query embeddings
- document embeddings
- semantic retrieval
- top-k search

Implemented:
- semantic search system
- similarity-based retrieval

---

## ✅ Day 3 — Chunking

Learned:
- fixed chunking
- sentence chunking
- overlap chunking

Important Understanding:
- chunk quality directly affects retrieval quality
- overlap helps preserve context

Implemented:
- chunk creation experiments
- overlap-based chunk retrieval

---

## ✅ Day 4–6 — Retrieval Experiments

Practical experiments with:
- embeddings
- cosine similarity
- vector search
- chunk retrieval
- semantic matching

Focused on understanding:
- how retrievers work internally
- how retrieval quality changes with chunking

---

## ✅ Day 7 — Local LLM Setup

Learned:
- role of LLM in RAG
- local vs API-based LLMs
- Ollama basics
- prompt engineering
- hallucination

Implemented:
- TinyLlama setup using Ollama
- Python to local LLM interaction
- prompt-response workflow

---

## ✅ Day 8 — Naive RAG Theory

Learned complete RAG pipeline:

Documents
→ Chunking
→ Embeddings
→ Vector Store
→ Query Embedding
→ Similarity Search
→ Retrieved Context
→ Prompt Injection
→ LLM Response

Important Understanding:
- Retriever and Generator are separate components
- Retrieval quality directly affects answer quality

---

## ✅ Day 9 — LlamaIndex Introduction

Learned:
- LlamaIndex basics
- nodes
- VectorStoreIndex
- retrievers
- query engine

Understanding:
- frameworks automate RAG pipelines
- internally still depend on embeddings + retrieval

---

# 🔥 Current Practical Phase

## ✅ Day 10–11–12 — Naive RAG Full Practical Build

Implemented:
- document loading
- embedding generation
- vector similarity search
- top-k retrieval
- prompt injection
- local LLM response generation

Built:
- first complete local Naive RAG pipeline using Python + Ollama

Tech Stack:
- Python
- Ollama
- TinyLlama
- sentence-transformers
- scikit-learn
- numpy

---

# 🧠 Important Concepts Understood

- embeddings are semantic representations
- vector search retrieves meaning, not keywords
- chunking impacts retrieval performance
- RAG does not train the LLM
- RAG works using retrieval + context injection
- hallucination reduces with grounded context
- retrieval quality is critical for good generation
- top-k retrieval improves answer quality
- small LLMs can still hallucinate despite good retrieval

---


# 🎯 Objective

The purpose of this repository is to:
- document my RAG learning journey
- understand AI systems deeply
- build practical projects
- move towards advanced Generative AI engineering

---

# 🔹 Phase 5: Advanced Retrieval Concepts

---

### ✅ Day 14 — Multiple Documents in RAG

Learned:

* Multi-document retrieval
* Metadata handling
* Source tracking
* Top-k retrieval importance
* Context construction from multiple documents
* Noise and ambiguity challenges

---

### ✅ Day 15 — Evaluation Basics

Learned:

* Retrieval evaluation
* Generation evaluation
* Precision
* Recall
* Faithfulness
* Groundedness
* Hallucination detection
* LLM-as-a-Judge

---

### ✅ Day 16 — Re-ranking

Learned:

* Re-ranking pipeline
* Cross-Encoders
* Vector search limitations
* Retrieval accuracy improvement
* Precision improvement
* Modern RAG retrieval pipelines

---

### 🧠 Key Concepts Learned
Embeddings
Semantic Search
Chunking
Vector Retrieval
Local LLMs
Naive RAG
LlamaIndex
Metadata
Retrieval Evaluation
Faithfulness
Groundedness
Re-ranking
Cross-Encoders


### ⚙️ Tools & Technologies
Python
scikit-learn
Sentence Transformers
Ollama
TinyLlama
LlamaIndex
Vector Search
Cosine Similarity