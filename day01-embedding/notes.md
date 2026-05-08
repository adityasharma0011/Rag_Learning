# 📘 Day 1: Embeddings 101

## 🧠 What are Embeddings?

Embeddings are numerical representations (vectors) of text that capture the **meaning** of words or sentences.

👉 Example:
"I love AI" → [0.21, -0.45, 0.88, ...]

---

## ❓ Why do we need Embeddings?

Computers cannot understand text directly.

* Human: understands meaning ✔
* Machine: sees only text ❌

👉 Solution: Convert text → numbers while preserving meaning

---

## 🔑 Key Idea

👉 Similar meaning → Similar vectors
👉 Different meaning → Distant vectors

---

## 📊 Example

| Sentence    | Meaning  | Similarity |
| ----------- | -------- | ---------- |
| I love AI   | Positive | High       |
| I like ML   | Positive | High       |
| I hate rain | Negative | Low        |

---

## 🔢 What is a Vector?

A vector is a list of numbers representing a sentence in a multi-dimensional space.

---

## 🧠 Types of Embeddings

### 🔹 Word Embeddings

* Represent individual words
* Example: Word2Vec, GloVe

### 🔹 Sentence Embeddings (Important)

* Represent full sentences
* Used in RAG systems

---

## ⚙️ Where are Embeddings used?

* Semantic Search 🔍
* Chatbots 🤖
* Recommendation Systems 🎯
* RAG (Retrieval-Augmented Generation) 📄

---

## 🔥 Role in RAG (Very Important)

RAG uses embeddings to find relevant information.

### Flow:

1. User query → embedding
2. Documents → embeddings
3. Similarity search
4. Retrieve relevant data
5. LLM generates answer

---

## 📐 Similarity Measurement

### Cosine Similarity

* 1 → very similar
* 0 → unrelated
* -1 → opposite

---

## 🎯 Example

Query: "I want to learn AI"

| Document             | Match          |
| -------------------- | -------------- |
| AI is the future     | ✔ Relevant     |
| Football match today | ❌ Not relevant |

---

## ⚠️ Important Points

* Embeddings match **meaning**, not keywords
* Better than traditional keyword search
* Still not perfect (can miss context)

---

## 🎯 Key Takeaways

* Embeddings convert text into meaningful numerical vectors
* Similar sentences are placed close in vector space
* They are the foundation of modern AI systems like RAG

---

## 💡 My Understanding

Embeddings help machines understand text by converting it into vectors, allowing comparison based on meaning rather than exact words.

---
