# 📘 Day 3: Chunking

## 🧠 What is Chunking?

Chunking is the process of splitting large documents into smaller, meaningful pieces (chunks) so they can be efficiently processed and retrieved.

---

## ❓ Why do we need Chunking?

Large documents cannot be directly used in RAG systems because:

* LLMs have token limits
* Processing large text is slow and inefficient
* Retrieval becomes inaccurate

👉 Solution: Break text into smaller parts (chunks)

---

## 🔑 Key Idea

👉 Instead of sending the entire document to the model, we send only the **most relevant chunk**.

---

## 🔍 Example

### Full Document:

AI is a field of computer science. Machine learning is a subset of AI. Deep learning uses neural networks.

---

### After Chunking:

* Chunk 1 → AI is a field of computer science
* Chunk 2 → Machine learning is a subset of AI
* Chunk 3 → Deep learning uses neural networks

👉 Now vector search retrieves only relevant chunk

---

## ⚙️ Role in RAG (Very Important)

### Flow:

1. Load document
2. Apply chunking
3. Convert chunks → embeddings
4. Perform vector search
5. Retrieve relevant chunks
6. Pass to LLM for answer

👉 Chunking directly affects retrieval quality

---

## 📐 Types of Chunking

### 🔹 Fixed-size Chunking

* Splits text into equal-sized chunks
* Simple but may break context

---

### 🔹 Semantic Chunking

* Splits based on meaning or sentences
* Preserves context better

---

### 🔹 Overlapping Chunking (Important)

Chunks share some overlapping content

Example:

* Chunk 1 → words 0–100
* Chunk 2 → words 80–180

👉 Helps maintain context across chunks

---

## ⚖️ Chunk Size Trade-off

### ❌ Too Small

* Loss of context
* Incomplete information

### ❌ Too Large

* Irrelevant data included
* Slower retrieval

👉 Balanced chunk size is important

---

## 🔥 Why Chunking Matters

* Improves retrieval accuracy
* Reduces noise
* Handles large documents efficiently
* Works within token limits

---

## ⚠️ Common Mistakes

* Random splitting without meaning
* No overlap between chunks
* Using very large chunks
* Ignoring context boundaries

---

## 🎯 Key Takeaways

* Chunking breaks large text into smaller parts
* It enables efficient and accurate retrieval in RAG
* Overlapping and proper chunk size are critical
* Better chunking → better RAG performance

---

## 💡 My Understanding

Chunking is essential for RAG because it allows the system to retrieve only the most relevant portions of a document instead of processing the entire text.

---
