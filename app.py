import gradio as gr
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

if not API_KEY:
    raise ValueError("❌ API KEY NOT FOUND. Check your .env file.")

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=API_KEY
)

SYSTEM_PROMPT = """
You are a practical assistant for freelancers.
Be clear, concise, and useful.
"""

def generate_response(prompt):
    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        response = client.chat_completion(
            messages=messages,
            max_tokens=1000,
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {str(e)}"

def respond(message, history):
    history = history or []

    reply = generate_response(message)

    # ✅ Dict format, no type= argument needed in Gradio 6
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})

    return "", history

with gr.Blocks(title="AI Chatbot") as demo:
    gr.Markdown("# 💬 AI Chatbot (API Version)")

    chatbot = gr.Chatbot()  # ✅ No type argument — Gradio 6 uses dicts by default
    msg = gr.Textbox(placeholder="Type your message here...")

    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

demo.launch()