# 📘 Day 14: Multiple Documents in RAG

---

## 🧠 What is Multiple Document RAG?

Multiple-document RAG means retrieving relevant chunks from many different documents instead of searching inside only one document.

---

## 🔥 Why is it Important?

Real-world RAG systems do not work with only one document.

Examples:

* company knowledge bases
* PDFs
* policies
* research papers
* FAQs

👉 The system must retrieve relevant information from all available documents.

---

## 🔁 Multiple Document RAG Pipeline

Multiple Documents
→ Chunking
→ Embeddings
→ Metadata Attachment
→ Vector Store
→ Query Embedding
→ Similarity Search
→ Top Relevant Chunks
→ LLM
→ Final Answer

---

## ⚙️ Step-by-step Flow

---

### 🔹 1. Multiple Documents

Input data can include:

* PDFs
* websites
* notes
* databases

---

### 🔹 2. Chunking

All documents are split into smaller chunks.

👉 Improves retrieval quality
👉 Handles token limits

---

### 🔹 3. Embeddings

Each chunk is converted into a vector representation.

👉 Similar meaning → similar vectors

---

### 🔹 4. Metadata (Very Important)

Metadata is extra information stored with chunks.

Example:

```json
{
  "source": "policy.pdf",
  "page": 4
}
```

---

## 🔥 Why Metadata is Important?

Metadata helps with:

* source tracking
* filtering
* citations
* debugging retrieval

---

## 🔹 5. Vector Store

All chunk embeddings from multiple documents are stored together.

Examples:

* FAISS
* Pinecone
* ChromaDB

---

## 🔹 6. Query Embedding

User query is converted into an embedding.

---

## 🔹 7. Similarity Search

The system compares:

* query embedding
* all chunk embeddings from all documents

👉 Retrieves the most relevant chunks.

---

## 🔹 8. Top-K Retrieval

Multiple relevant chunks are usually retrieved.

Example:

```python
top_k = 5
```

👉 Important because one chunk may not contain complete information.

---

## 🔹 9. Context Construction

Retrieved chunks from different documents are combined and passed to the LLM.

Example:

* chunk from FAQ.pdf
* chunk from policy.pdf
* chunk from rules.pdf

👉 Together they form the final context.

---

## ⚠️ Challenges in Multiple Documents

### ❌ Noise

More documents increase irrelevant retrieval.

---

### ❌ Ambiguity

Same words may exist in different contexts.

Example:

* river bank
* financial bank

---

### ❌ Duplicate Information

Different documents may contain repeated information.

---

### ❌ Context Window Limit

LLMs can only process limited context at once.

---

## 🎯 Why Retrieval Quality Matters More

In multiple-document RAG:

* search space becomes larger
* irrelevant chunks are easier to retrieve

👉 Better retrieval = better answers

---

## 🔥 Source Attribution

Real systems often display:

* source document
* page number

👉 Metadata enables this.

---

## 🧠 Single vs Multiple Document RAG

| Single Document    | Multiple Documents     |
| ------------------ | ---------------------- |
| Easier retrieval   | More complex retrieval |
| Less noise         | More noise             |
| Small search space | Large search space     |

---

## 🎯 Key Takeaways

* Multiple-document RAG searches across many documents
* Metadata becomes very important
* Top-k retrieval is critical
* Retrieval quality affects final answer quality
* Source tracking improves transparency

---

## 💡 My Understanding

Multiple-document RAG retrieves relevant chunks from many documents using embeddings and metadata, then combines them as context for the LLM to generate grounded responses.

---
