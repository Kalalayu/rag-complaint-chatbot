# src/generator.py

from transformers import pipeline

print("🚀 Loading T5 model...")
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1  # CPU
)

def generate_answer(prompt: str) -> str:
    output = generator(
        prompt,
        max_length=256,
        do_sample=False
    )
    return output[0]["generated_text"]
    model="google/flan-t5-small",
    do_sample=True,
    temperature=0.7,
    max_new_tokens=100
)

def generate_answer(question: str) -> str:
    """
    Generate an answer from the question using the LLM.
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
