def answer_question(question: str):
    """
    Args:
        question (str)

    Returns:
        answer (str)
        sources (list of dict)
    """

    # Placeholder – replace with real RAG logic
    answer = (
        "Common complaints include unexpected fees, billing disputes, "
        "and slow customer support responses."
    )

    sources = [
        {
            "text": "I was charged fees I was never informed about...",
            "product_category": "Credit Card",
            "issue": "Billing dispute",
            "company": "Bank ABC",
            "date_received": "2022-06-18"
        }
    ]

    return answer, sources
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
