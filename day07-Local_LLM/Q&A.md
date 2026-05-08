# 📘 Day 7: Local LLM – Important Q&A

---

## ❓ 1. What is the role of LLM in RAG?

LLM generates the final answer using the retrieved chunks as context. It does not perform retrieval.

---

## ❓ 2. What is the difference between Local and API-based LLM?

Local LLM runs on your system (offline, private but slower), while API-based LLMs run on the cloud (faster, more powerful but require internet and may have costs).

---

## ❓ 3. What is a Prompt?

A prompt is an instruction given to the LLM to guide how it should generate the response.

---

## ❓ 4. What is Context?

Context is the retrieved relevant information provided to the LLM along with the query to ensure accurate and grounded answers.

---

## ❓ 5. What is Hallucination?

Hallucination occurs when an LLM generates incorrect or fabricated information confidently.

---

## ❓ 6. How does RAG reduce hallucination?

RAG provides relevant context to the LLM, which helps it generate more accurate and factual responses.

---

## ❓ 7. Why is context important?

Context ensures that the LLM generates responses based on actual data rather than guessing.

---

## 🎯 Summary

* LLM = Answer generator
* Context = Retrieved knowledge
* Prompt = Instruction
* RAG = Combines retrieval + generation

---
