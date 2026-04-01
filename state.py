import streamlit as st
from datetime import datetime
import uuid
import re


def init_state() -> None:
    if "chats" not in st.session_state:
        first_id = str(uuid.uuid4())
        st.session_state.chats = {
            first_id: {
                "title": "New Chat",
                "messages": [],
                "created_at": datetime.now().strftime("%H:%M"),
            }
        }
        st.session_state.current_chat_id = first_id

    if "current_chat_id" not in st.session_state:
        st.session_state.current_chat_id = list(st.session_state.chats.keys())[0]


def create_new_chat() -> None:
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": [],
        "created_at": datetime.now().strftime("%H:%M"),
    }
    st.session_state.current_chat_id = chat_id
    st.rerun()


def switch_chat(chat_id: str) -> None:
    if chat_id in st.session_state.chats:
        st.session_state.current_chat_id = chat_id
        st.rerun()


def delete_chat(chat_id: str) -> None:
    if chat_id in st.session_state.chats and len(st.session_state.chats) > 1:
        del st.session_state.chats[chat_id]
        st.session_state.current_chat_id = list(st.session_state.chats.keys())[0]
        st.rerun()


def _smart_chat_title(content: str) -> str:
    text = content.strip()
    if not text:
        return "Untitled"

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    for line in lines:
        if line.lower().startswith("subject:"):
            subject = line.split(":", 1)[1].strip()
            return subject[:40] if subject else "New Chat"

    first_line = lines[0] if lines else text
    first_line = re.sub(r"\s+", " ", first_line)

    if len(first_line) > 40:
        first_line = first_line[:40].rstrip() + "..."
    return first_line


def save_message(chat_id: str, role: str, content: str) -> None:
    st.session_state.chats[chat_id]["messages"].append(
        {"role": role, "content": content}
    )

    if role == "user" and st.session_state.chats[chat_id]["title"] == "New Chat":
        st.session_state.chats[chat_id]["title"] = _smart_chat_title(content)