# 📘 Day 7: Local LLM Setup

---

## 🧠 What is an LLM?

A Large Language Model (LLM) is an AI model that can:

* Understand text
* Generate human-like responses

Examples:

* GPT (ChatGPT)
* LLaMA
* Mistral

---

## 🔥 Role of LLM in RAG

In a RAG system:

1. User Query
2. → Vector Search (retrieve chunks)
3. → LLM (generate answer using context)

👉 LLM does **not retrieve data**, it only generates answers.

---

## 🔑 Key Idea

👉
LLM = Generator
Vector Search = Retriever

👉 Together they form a RAG system.

---

## ⚙️ Local LLM vs API-based LLM

### 🔹 Local LLM

* Runs on your system
* Works offline
* Private (data stays local)

❌ Cons:

* Slower
* Requires setup
* Limited performance

---

### 🔹 API-based LLM

* Runs on cloud
* Requires internet
* More powerful

❌ Cons:

* Paid
* Data privacy concerns

---

## 🧠 What is a Prompt?

A prompt is an instruction given to the LLM to guide its response.

### Example:

Answer the question based on the context below:
Context: {retrieved chunks}
Question: {user query}

---

## 🧠 What is Context?

Context is the relevant information retrieved (chunks) and passed to the LLM along with the query.

👉 Without context:

* LLM may hallucinate ❌

👉 With context:

* Accurate answers ✔

---

## ⚠️ Hallucination

When an LLM generates incorrect or made-up information confidently.

👉 RAG reduces hallucination by providing context.

---

## 🔁 RAG Flow with LLM

User Query
→ Embedding
→ Vector Search
→ Retrieve Chunks
→ LLM (with context + prompt)
→ Final Answer

---

## 🎯 Key Takeaways

* LLM generates answers, not retrieve data
* Context is critical for accuracy
* Prompt controls LLM behavior
* Local LLM allows private and offline usage
* RAG reduces hallucination

---

## 💡 My Understanding

LLMs generate answers based on provided context, and in RAG systems, they rely on retrieved chunks to produce accurate and grounded responses.

---
