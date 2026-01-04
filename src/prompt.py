def build_prompt(question: str, chunks: list) -> str:
    context = "\n\n".join(
        f"- {c['text']}" for c in chunks
    )

    return f"""
You are a financial complaints analysis assistant.

Context:
{context}

Question:
{question}

Answer concisely and factually.
"""
