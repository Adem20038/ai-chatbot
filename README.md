# AI Chatbot V1 — Hugging Face API + Gradio

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Gradio](https://img.shields.io/badge/Gradio-6.x-orange?style=flat-square)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Inference%20API-yellow?style=flat-square&logo=huggingface)
![Status](https://img.shields.io/badge/Status-V1%20Prototype-lightgrey?style=flat-square)

---

## Overview

This is the first version of an AI chatbot I built while learning how to integrate large language models into real applications. It's not perfect, but it works end-to-end — from sending a message in the browser to getting a response from a hosted LLM through the Hugging Face Inference API.

The main things I wanted to get right in this version were: connecting to an external AI API, keeping credentials secure, and having something actually runnable in the browser without overcomplicating the setup.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| UI | Gradio |
| LLM Provider | Hugging Face Inference API |
| Env Management | python-dotenv |
| HTTP | requests |

---

## What it does

- Sends user messages to a hosted LLM via the Hugging Face Inference API
- Displays the conversation in a simple browser interface built with Gradio
- Keeps the API key out of the code using a `.env` file
- Runs entirely on CPU — no GPU needed

---

## Project Structure
chatBot/
│
├── app.py    # main application
├── .env      # API key (not committed)
├── requirements.txt     # dependencies
├── .gitignore
└── README.md
---

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file at the root of the project:

```env
HUGGINGFACE_API_KEY=your_api_key_here
```

Then run:

```bash
python app.py
```

The app will open at `http://127.0.0.1:7860`

---

## Known Limitations

This is an early version and there's a lot it doesn't do yet:

- No memory — each message is treated independently
- No RAG or external knowledge source
- The UI is Gradio's default, nothing custom
- Prompt engineering is minimal
- Completely dependent on Hugging Face's API being available

---

## Roadmap

V2 — add RAG and improve how the conversation context is handled

V3 — replace the Gradio UI with a custom frontend, add file upload support

V4 — deploy it publicly (Hugging Face Spaces or Render), add response streaming

---

## Why I built this

I wanted to go beyond tutorials and build something that actually runs. This project helped me understand how API-based LLM integration works, how to structure a small AI project cleanly, and how to manage things like secrets and dependencies in a way that's ready for a real repo.

---

## Status

Version 1 — works, but rough around the edges. Actively improving it.