# src/evaluate.py
import pandas as pd
from src.generator import generate_answer

# -------------------------
# STEP 1: Define evaluation questions
# -------------------------
evaluation_questions = [
    "Why did customer X complain about their loan?",
    "Which complaints are related to delayed payments?",
    "Are there recurring issues with the mobile app?",
    "What was the main reason for complaints in January 2025?",
    "Which complaints were resolved successfully?"
]

evaluation_results = []

# -------------------------
# STEP 2: Generate answers
# -------------------------
for q in evaluation_questions:
    print(f"\nQuestion: {q}")
    answer = generate_answer(q)  # call your generator
    print("Answer:", answer)

    evaluation_results.append({
        "Question": q,
        "Generated Answer": answer,
        "Quality Score": None,
        "Comments": ""
    })

# -------------------------
# STEP 3: Save evaluation table
# -------------------------
df = pd.DataFrame(evaluation_results)
df.to_csv("evaluation_table.csv", index=False)
print("\nEvaluation table saved as evaluation_table.csv")
