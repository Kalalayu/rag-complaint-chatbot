# src/generator.py
from transformers import pipeline

# Use text2text-generation for T5 models
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",  # small model, works on CPU
    do_sample=True,
    temperature=0.7,
    max_new_tokens=80
)

def generate_answer(question: str) -> str:
    prompt = f"Answer the following question clearly:\n\n{question}\nAnswer:"
    output = llm(prompt)
    return output[0]["generated_text"]
