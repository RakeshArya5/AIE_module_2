# Module 2: Prompt Engineering Chatbot

A small Streamlit chatbot (using OpenAI's `gpt-4o-mini`) that shows how much
the **system prompt** changes an AI's answers.

## What this project demonstrates

- **Structured vs unstructured prompting** - a plain prompt vs a designed one
- **Few-shot examples** - showing the model one sample answer to copy
- **Output control** - forcing a fixed format (a summary plus a table)
- **Guard rules** - telling the model to admit when it can't or shouldn't answer

## Files

| File | Purpose |
|---|---|
| `app.py` | The Streamlit chat interface |
| `prompts.py` | The Basic and Engineered system prompts |
| `helpers.py` | The `ask()` function that calls the OpenAI API |

## Setup

1. Activate the virtual environment (Windows):
   ```
   venv\Scripts\activate
   ```
   On Mac/Linux: `source venv/bin/activate`
2. Install the packages:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env`, then open `.env` and replace `your_key_here`
   with your real OpenAI API key.

## Run

```
streamlit run app.py
```

## Try this

Ask the same question in **Basic Mode**, then switch to **Engineered Mode** and
ask it again. Compare the answers: format, length, and how each mode handles
off-topic questions (try "What's a good pasta recipe?").
