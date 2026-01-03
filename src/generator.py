# src/generator.py
from transformers import pipeline

# Load small CPU-friendly model
llm = pipeline(
    "text-generation",
    model="google/flan-t5-small",  # tiny enough for CPU
    do_sample=True,
    temperature=0.7,
    max_new_tokens=100
)

def generate_answer(question: str):
    """
    Generate an answer and dummy sources (for now).
    """
    prompt = f"Answer the following question clearly:\n\n{question}\nAnswer:"
    output = llm(prompt)
    answer = output[0]["generated_text"]
    
    # Dummy sources - you can replace with actual RAG retrieval
    sources = [
        "Source 1: Company complaint log",
        "Source 2: Customer email records"
    ]
    
    return answer, sources
