# app/main.py
import gradio as gr
from src.generator import generate_answer

# Store chat history
chat_history = []

def ask_question(user_input):
    answer, sources = generate_answer(user_input)
    # Update chat history
    chat_history.append((user_input, answer, sources))
    formatted_history = ""
    for q, a, s in chat_history:
        formatted_history += f"**Q:** {q}\n**A:** {a}\nSources: {', '.join(s)}\n\n"
    return formatted_history

def clear_chat():
    chat_history.clear()
    return ""

# Build Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## RAG Complaint Chatbot (CPU-friendly)")

    user_input = gr.Textbox(label="Enter your question", placeholder="Type your question here...")
    output = gr.Textbox(label="Chat History", placeholder="Answers will appear here...", lines=15)
    
    with gr.Row():
        ask_btn = gr.Button("Ask")
        clear_btn = gr.Button("Clear")
    
    ask_btn.click(fn=ask_question, inputs=user_input, outputs=output)
    clear_btn.click(fn=clear_chat, inputs=None, outputs=output)

if __name__ == "__main__":
    demo.launch()
