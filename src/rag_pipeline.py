# src/rag_pipeline.py

from src.retriever import retrieve_chunks
from src.prompt import build_prompt
from src.generator import generate_answer


def run_rag(question: str) -> dict:
    docs = retrieve_chunks(question)

    prompt = build_prompt(question, docs)
    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": docs
    }
