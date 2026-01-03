# app/main.py
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gradio as gr
from src.generator import generate_answer

def ask_question(user_input):
    return generate_answer(user_input)

def run_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## RAG Complaint Chatbot")
        user_input = gr.Textbox(label="Enter your question")
        output = gr.Textbox(label="Answer")
        submit = gr.Button("Ask")
        submit.click(fn=ask_question, inputs=user_input, outputs=output)
    demo.launch()

if __name__ == "__main__":
    run_interface()
