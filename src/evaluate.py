# src/evaluate.py

import pandas as pd
from src.rag_pipeline import run_rag

evaluation_questions = [
    "Why did customers complain about loans?",
    "Which complaints are related to delayed payments?",
    "Are there recurring issues with the mobile app?",
    "What are the most common complaint themes?",
    "Which complaints mention resolution?"
]

results = []

for q in evaluation_questions:
    print(f"\n❓ Question: {q}")

    output = run_rag(q)

    print("✅ Answer:", output["answer"])
    print("📚 Sources used:", len(output["sources"]))

    results.append({
        "Question": q,
        "Answer": output["answer"],
        "Num Sources": len(output["sources"])
    })

df = pd.DataFrame(results)
df.to_csv("evaluation_results.csv", index=False)

print("\n📄 evaluation_results.csv saved")
