import gradio as gr
from src.rag_pipeline import answer_question


def gradio_chat(question):
    answer, sources = answer_question(question)

    # Format sources for display
    source_text = ""
    for i, src in enumerate(sources[:3], 1):
        source_text += (
            f"### Source {i}\n"
            f"**Product:** {src['product_category']}\n\n"
            f"{src['text']}\n\n"
            f"*Issue:* {src['issue']} | "
            f"*Company:* {src['company']} | "
            f"*Date:* {src['date_received']}\n\n"
            "---\n\n"
        )

    return answer, source_text


with gr.Blocks(title="CrediTrust Complaint Assistant") as demo:
    gr.Markdown("# 💬 CrediTrust Intelligent Complaint Assistant")
    gr.Markdown(
        "Ask questions about customer complaints across Credit Cards, "
        "Personal Loans, Savings Accounts, and Money Transfers."
    )

    question_input = gr.Textbox(
        label="Enter your question",
        placeholder="e.g. Why are customers unhappy with Credit Cards?"
    )

    ask_button = gr.Button("Ask")
    clear_button = gr.Button("Clear")

    answer_output = gr.Markdown(label="Answer")
    sources_output = gr.Markdown(label="Sources")

    ask_button.click(
        fn=gradio_chat,
        inputs=question_input,
        outputs=[answer_output, sources_output]
    )

    clear_button.click(
        fn=lambda: ("", ""),
        inputs=None,
        outputs=[answer_output, sources_output]
    )

demo.launch(share=True)

