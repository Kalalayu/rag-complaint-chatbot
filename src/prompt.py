def build_prompt(question, retrieved_chunks):
    context = "\n".join(retrieved_chunks)
    prompt = f"""
You are a financial analyst assistant for CrediTrust. Your task is to answer questions about customer complaints. 
Use only the following retrieved complaint excerpts to answer the user's question. 
If the context doesn't contain the answer, state that you don't have enough information.

Context: {context}

Question: {question}

Answer:
"""
    return prompt
