import streamlit as st
from groq_client import generate_email_reply
from prompts import build_email_reply_prompt
from state import init_state, create_new_chat, save_message, switch_chat, delete_chat
from ui import (
    apply_kintsugi_theme,
    render_ivurd_intro,
    render_sidebar,
    render_header,
    render_welcome_screen,
    render_chat_messages,
    render_chat_input_box,
    render_message_actions,
    render_empty_state,
)

st.set_page_config(
    page_title="IVURD Email Reply AI",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_state()
apply_kintsugi_theme()
render_ivurd_intro()
render_header()


# ---------------- INTRO (NETFLIX STYLE) ----------------
if "intro_done" not in st.session_state:
    render_ivurd_intro()   # 🔥 shows animation first
    st.session_state.intro_done = True

# ---------------- INIT ----------------
init_state()
apply_kintsugi_theme()
#render_header()

# ---------------- SIDEBAR ----------------
sidebar_action = render_sidebar(
    chats=st.session_state.chats,
    current_chat_id=st.session_state.current_chat_id,
)

if sidebar_action["type"] == "new_chat":
    create_new_chat()

elif sidebar_action["type"] == "switch_chat":
    switch_chat(sidebar_action["chat_id"])

elif sidebar_action["type"] == "delete_chat":
    delete_chat(sidebar_action["chat_id"])

# ---------------- CURRENT CHAT ----------------
current_chat = st.session_state.chats[st.session_state.current_chat_id]

# ---------------- EMPTY STATE ----------------
if not current_chat["messages"]:
    render_welcome_screen()
    render_empty_state()

# ---------------- CHAT DISPLAY ----------------
render_chat_messages(current_chat["messages"])

# ---------------- ACTIONS ----------------
action = render_message_actions()

if action == "retry_last":
    msgs = current_chat["messages"]

    if len(msgs) >= 2 and msgs[-1]["role"] == "assistant":
        while msgs and msgs[-1]["role"] == "assistant":
            msgs.pop()

        user_message = msgs[-1]["content"] if msgs else ""

        if user_message:
            prompt = build_email_reply_prompt(user_message)

            with st.spinner("Generating reply..."):
                reply = generate_email_reply(prompt)

            save_message(st.session_state.current_chat_id, "assistant", reply)

        st.rerun()

elif action == "clear_chat":
    current_chat["messages"] = []
    st.rerun()

# ---------------- INPUT ----------------
user_input = render_chat_input_box()

if user_input:
    if not user_input.strip():
        st.warning("Please enter email context first.")
    else:
        save_message(st.session_state.current_chat_id, "user", user_input)

        prompt = build_email_reply_prompt(user_input)

        with st.spinner("Generating reply..."):
            reply = generate_email_reply(prompt)

        save_message(st.session_state.current_chat_id, "assistant", reply)

        st.rerun()