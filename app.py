"""app.py - Streamlit chatbot that compares Basic vs Engineered prompts.

Run with:  streamlit run app.py
"""

import streamlit as st

from helpers import ask
from prompts import BASIC_SYSTEM_PROMPT, ENGINEERED_SYSTEM_PROMPT

st.set_page_config(page_title="Module 2: Prompt Engineering Chatbot")
st.title("Module 2: Prompt Engineering Chatbot")

# Streamlit re-runs this whole file on every click, so we keep the chat
# history in session_state, which survives between runs.
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Sidebar ----------
mode = st.sidebar.radio("Choose Mode", ["Basic Mode", "Engineered Mode"])
st.sidebar.caption(
    "Basic Mode: plain prompt, free-form answers. "
    "Engineered Mode: analyst role, few-shot example, fixed format, guard rule."
)

if st.sidebar.button("Clear chat"):
    st.session_state.messages = []

# Pick the system prompt that matches the selected mode
if mode == "Basic Mode":
    system_prompt = BASIC_SYSTEM_PROMPT
else:
    system_prompt = ENGINEERED_SYSTEM_PROMPT

# ---------- Show the chat so far ----------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])  # markdown lets the table render

# ---------- Handle a new question ----------
user_input = st.chat_input("Ask a question...")

if user_input:
    # 1) Save and show the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2) Ask the model, using the full history so it remembers the chat
    with st.chat_message("assistant"):
        reply = ask(st.session_state.messages, system_prompt)
        st.markdown(reply)

    # 3) Save the reply so it appears in the history next time
    st.session_state.messages.append({"role": "assistant", "content": reply})
