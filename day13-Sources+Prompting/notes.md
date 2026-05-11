````md id="f23kls"
# 📘 Day 13: Sources + Prompting in RAG

---

## 🧠 What are Sources in RAG?

Sources are the retrieved chunks or documents used by the LLM to generate answers.

Example:

Question:
```text
What is RAG?
````

Retrieved Source:

```text
RAG stands for Retrieval-Augmented Generation.
```

---

## 🔥 Why Sources Matter?

Sources help:

* reduce hallucination
* improve trust
* verify answers
* provide grounded responses

Without sources:
LLM mostly guesses.

With sources:
LLM answers using retrieved information.

---

## 🔁 RAG with Sources Flow

Documents
→ Chunking
→ Embeddings
→ Vector Store
→ Query
→ Similarity Search
→ Retrieve Sources
→ Prompt + Context
→ LLM
→ Final Answer

---

## 🧠 What is Prompting?

Prompting means giving instructions to the LLM.

The prompt controls:

* behavior
* answer style
* restrictions
* response format

---

## 🔥 Why Prompting is Important in RAG?

Even if retrieval is good, bad prompts can cause:

* hallucination
* wrong answers
* context ignoring

Good prompts improve grounding.

---

## 🧠 Basic RAG Prompt Structure

A RAG prompt usually contains:

1. Instruction
2. Context
3. Question

Example:

```text
Use the provided context to answer the question.

Context:
{retrieved_text}

Question:
{query}
```

---

## ⚙️ Prompt Components

### 🔹 1. Role

Defines assistant behavior.

Example:

```text
You are a helpful AI assistant.
```

---

### 🔹 2. Instruction

Defines rules.

Example:

```text
Answer only from the provided context.
```

---

### 🔹 3. Context

Retrieved chunks inserted into the prompt.

Example:

```text
Context:
{retrieved_text}
```

---

### 🔹 4. Question

User query.

Example:

```text
Question:
{query}
```

---

## 🔥 Weak Prompt vs Strong Prompt

### ❌ Weak Prompt

```text
Answer the question.
```

Problem:

* vague instruction
* hallucination possible

---

### ✅ Strong Prompt

```text
Answer only from the provided context.
If answer is not available, say:
"I don't know."
```

Benefits:

* grounded answers
* better control
* less hallucination

---

## 🧠 Top-k Retrieval + Prompting

Instead of one chunk, multiple chunks are retrieved.

Example:

```text
Context:
chunk 1
chunk 2
chunk 3
```

👉 Gives richer information to the LLM.

---

## 🧠 Important Practical Learning

We observed:

Good Retrieval
+
Bad Prompt
==========

Weak Answers

---

Good Retrieval
+
Good Prompt
===========

Better Answers

---

## 🧠 Important Realization

RAG does NOT retrain the LLM.

Instead:

👉 retrieved context is injected into the prompt

This is called:

# Prompt Augmentation

---

## 🎯 Core Understanding

Sources decide:
👉 what information the LLM gets

Prompts decide:
👉 how the LLM uses that information

Both together improve RAG quality.

---

