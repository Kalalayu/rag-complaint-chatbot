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
