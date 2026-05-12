# 📘 Day 14: Multiple Documents – Important Q&A

---

## ❓ 1. What is Multiple Document RAG?

Multiple-document RAG retrieves relevant chunks from many documents instead of searching inside only one document.

---

## ❓ 2. Why is Metadata important?

Metadata stores additional information such as:

* source file
* page number
* author

👉 It helps with source tracking, filtering, and citations.

---

## ❓ 3. Why is Retrieval harder in Multiple Documents?

Because:

* search space becomes larger
* irrelevant chunks increase
* ambiguity and noise become more common

---

## ❓ 4. Why is Top-K retrieval important?

Top-k retrieval helps retrieve multiple relevant chunks because a single chunk may not contain complete information.

---

## ❓ 5. What problems occur in Multiple Document RAG?

Common problems:

* noise
* ambiguity
* duplicate information
* context window limitations

---

## ❓ 6. Why does Retrieval Quality matter more in Multiple Docs?

The LLM depends on retrieved chunks for answer generation, so poor retrieval leads to inaccurate or irrelevant answers.

---

## ❓ 7. What is Source Attribution?

Source attribution means showing where the retrieved information came from.

Example:

* policy.pdf
* page 4

---

## ❓ 8. What is the role of Metadata in source tracking?

Metadata connects retrieved chunks with their original document source and additional details.

---

## 🎯 Summary

* Multiple-document RAG searches across many documents
* Metadata is critical for tracking and filtering
* Retrieval becomes more difficult due to larger search space
* Top-k retrieval improves context quality

---
