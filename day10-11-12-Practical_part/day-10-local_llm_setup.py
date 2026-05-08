# =========================================================
# Day 10: Local LLM Setup Practical
# =========================================================

# ---------------------------------------------------------
# Step 1: Import Ollama
# ---------------------------------------------------------

import ollama


# ---------------------------------------------------------
# Step 2: Basic Chat with Local LLM
# ---------------------------------------------------------

response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            'role': 'user',
            'content': 'What is Machine Learning?'
        }
    ]
)

print("\n--- Basic Response ---")
print(response['message']['content'])


# ---------------------------------------------------------
# Step 3: Prompt Experiment
# ---------------------------------------------------------

response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            'role': 'user',
            'content': 'Explain embeddings in 1 line.'
        }
    ]
)

print("\n--- Short Prompt Response ---")
print(response['message']['content'])


# ---------------------------------------------------------
# Step 4: Deep Prompt Experiment
# ---------------------------------------------------------

response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            'role': 'user',
            'content': 'Explain embeddings deeply with examples.'
        }
    ]
)

print("\n--- Deep Prompt Response ---")
print(response['message']['content'])


# ---------------------------------------------------------
# Step 5: System Prompt
# ---------------------------------------------------------

response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            'role': 'system',
            'content': 'You are a concise AI tutor. Answer in maximum 3 lines.'
        },
        {
            'role': 'user',
            'content': 'Explain vector search simply in 1 sentence.'
        }
    ]
)

print("\n--- System Prompt Response ---")
print(response['message']['content'])


# ---------------------------------------------------------
# Step 6: Compare Another Model (Optional)
# ---------------------------------------------------------

# response = ollama.chat(
#     model='mistral',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'What is chunking in RAG?'
#         }
#     ]
# )

# print("\n--- Mistral Model Response ---")
# print(response['message']['content'])

