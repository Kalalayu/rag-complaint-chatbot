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
