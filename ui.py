import streamlit as st


def render_ivurd_intro():
    st.markdown(
        """
        <style>
        #ivurd-intro {
            position: fixed;
            inset: 0;
            background: radial-gradient(circle at center, #0a0a0a 0%, #000 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 999999;
            animation: fadeOut 1s ease forwards;
            animation-delay: 4.8s;
        }

        .logo-container {
            position: relative;
            display: flex;
            gap: 8px;
            align-items: center;
            justify-content: center;
        }

        .letter {
            font-size: 5rem;
            font-weight: 900;
            color: #d4af37;
            opacity: 0;
            transform: translateY(40px) scale(0.85);
            text-shadow:
                0 0 10px rgba(212,175,55,0.3),
                0 0 25px rgba(212,175,55,0.2);
            animation: reveal 0.65s ease forwards;
        }

        .letter:nth-child(1) { animation-delay: 0.2s; }
        .letter:nth-child(2) { animation-delay: 0.5s; }
        .letter:nth-child(3) { animation-delay: 0.8s; }
        .letter:nth-child(4) { animation-delay: 1.1s; }
        .letter:nth-child(5) { animation-delay: 1.4s; }

        @keyframes reveal {
            0% {
                opacity: 0;
                transform: translateY(40px) scale(0.85);
                filter: blur(6px);
            }
            60% {
                opacity: 1;
                transform: translateY(-4px) scale(1.05);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
                filter: blur(0);
            }
        }

        .logo-container::after {
            content: "";
            position: absolute;
            top: 52%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 0%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #d4af37, transparent);
            animation: crackLine 1.2s ease forwards;
            animation-delay: 2.0s;
        }

        @keyframes crackLine {
            from { width: 0%; opacity: 0; }
            to { width: 115%; opacity: 1; }
        }

        @keyframes fadeOut {
            to {
                opacity: 0;
                visibility: hidden;
                pointer-events: none;
            }
        }
        </style>

        <div id="ivurd-intro">
            <div class="logo-container">
                <span class="letter">I</span>
                <span class="letter">V</span>
                <span class="letter">U</span>
                <span class="letter">R</span>
                <span class="letter">D</span>
            </div>
        </div>

        <audio autoplay>
            <source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True,
    )
def apply_kintsugi_theme() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #0b0b0b;
            --panel: #111111;
            --gold: #d4af37;
            --gold-bright: #f5d97a;
            --text: #f5f1e8;
            --muted: #b9b2a3;
            --border: rgba(212, 175, 55, 0.35);
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(212,175,55,0.08), transparent 28%),
                radial-gradient(circle at bottom right, rgba(212,175,55,0.06), transparent 25%),
                linear-gradient(135deg, #080808, #111111 45%, #090909);
            color: var(--text);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0c0c0c, #141414);
            border-right: 1px solid var(--border);
        }

        .ivurd-header {
            padding: 0.5rem 0 0.9rem 0;
            margin-bottom: 0.25rem;
        }

        .ivurd-title {
            font-size: 2.2rem;
            font-weight: 900;
            letter-spacing: 0.04em;
            color: var(--gold);
            text-shadow:
                0 0 10px rgba(212,175,55,0.45),
                0 0 24px rgba(212,175,55,0.18);
        }

        .ivurd-subtitle {
            color: var(--muted);
            font-size: 0.96rem;
            margin-top: 0.15rem;
        }

        .kintsugi-box {
            position: relative;
            background: linear-gradient(180deg, rgba(20,20,20,0.98), rgba(12,12,12,0.98));
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 14px 16px;
            margin-bottom: 14px;
            box-shadow:
                0 0 0 1px rgba(212,175,55,0.05),
                0 8px 22px rgba(0,0,0,0.35);
            overflow: hidden;
        }

        .kintsugi-box::before {
            content: "";
            position: absolute;
            inset: 0;
            border-radius: 18px;
            pointer-events: none;
            background:
                linear-gradient(
                    115deg,
                    transparent 0%,
                    transparent 26%,
                    rgba(212,175,55,0.06) 27%,
                    rgba(212,175,55,0.18) 28%,
                    transparent 29%,
                    transparent 100%
                );
        }

        .chat-user {
            background: linear-gradient(180deg, #171717, #111111);
            border-left: 3px solid var(--gold);
        }

        .chat-assistant {
            background: linear-gradient(180deg, #111111, #0c0c0c);
            border-left: 3px solid #8c6f1a;
        }

        .chat-role {
            color: var(--gold);
            font-weight: 700;
            margin-bottom: 8px;
            font-size: 0.92rem;
        }

        .chat-content {
            color: var(--text);
            line-height: 1.65;
            white-space: pre-wrap;
        }

        .welcome-card {
            text-align: center;
            padding: 2rem 1rem 1rem 1rem;
            margin-bottom: 1.2rem;
        }

        .welcome-card h2 {
            color: var(--gold);
            margin-bottom: 0.3rem;
        }

        .welcome-card p {
            color: var(--muted);
            margin: 0;
        }

        .sidebar-title {
            color: var(--gold);
            font-size: 1.2rem;
            font-weight: 800;
            margin-bottom: 0.6rem;
        }

        .recent-title {
            color: var(--gold-bright);
            font-size: 0.95rem;
            font-weight: 700;
            margin: 0.4rem 0 0.6rem 0;
        }

        .splash-wrap {
            position: relative;
            height: 110px;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            margin-bottom: 8px;
        }

        .splash-logo {
            font-size: 2.9rem;
            font-weight: 900;
            color: var(--gold);
            letter-spacing: 0.12em;
            animation: ivurdGlow 1.9s ease-in-out infinite alternate;
            text-shadow:
                0 0 10px rgba(212,175,55,0.45),
                0 0 22px rgba(212,175,55,0.28);
        }

        @keyframes ivurdGlow {
            0% {
                transform: scale(0.96);
                opacity: 0.84;
                text-shadow: 0 0 6px rgba(212,175,55,0.25);
            }
            100% {
                transform: scale(1.04);
                opacity: 1;
                text-shadow:
                    0 0 10px rgba(212,175,55,0.50),
                    0 0 24px rgba(212,175,55,0.35),
                    0 0 42px rgba(212,175,55,0.18);
            }
        }

        .stTextArea textarea, .stTextInput input {
            background: #121212 !important;
            color: #f6f1e8 !important;
            border: 1px solid rgba(212,175,55,0.35) !important;
            border-radius: 14px !important;
        }

        .stButton>button {
            background: linear-gradient(180deg, #1a1a1a, #111111) !important;
            color: #f5e6b8 !important;
            border: 1px solid rgba(212,175,55,0.4) !important;
            border-radius: 12px !important;
        }

        .stButton>button:hover {
            border-color: rgba(212,175,55,0.75) !important;
            box-shadow: 0 0 18px rgba(212,175,55,0.18);
            color: #fff3c8 !important;
            transform: translateY(-1px);
        }

        .muted-note {
            color: var(--muted);
            font-size: 0.9rem;
            margin-top: 0.4rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_splash_screen() -> None:
    st.markdown(
        """
        <div class="splash-wrap">
            <div class="splash-logo">IVURD</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown(
        """
        <div class="ivurd-header">
            <div class="ivurd-title">IVURD Email Reply AI</div>
            <div class="ivurd-subtitle">
                Generate polished email replies from your context with a ChatGPT-style layout.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(chats, current_chat_id):
    action = {"type": None, "chat_id": None}

    with st.sidebar:
        st.markdown('<div class="sidebar-title">✨ IVURD Chats</div>', unsafe_allow_html=True)

        if st.button("➕ New Chat", use_container_width=True, key="new_chat_btn"):
            action["type"] = "new_chat"
            return action

        st.markdown("---")
        st.markdown('<div class="recent-title">🕘 Recent</div>', unsafe_allow_html=True)

        for chat_id, chat in reversed(list(chats.items())):
            title = chat["title"]
            display_title = f"● {title}" if chat_id == current_chat_id else title

            col1, col2 = st.columns([4, 1])

            with col1:
                if st.button(display_title, key=f"chat_{chat_id}", use_container_width=True):
                    action["type"] = "switch_chat"
                    action["chat_id"] = chat_id
                    return action

            with col2:
                if len(chats) > 1:
                    if st.button("🗑️", key=f"del_{chat_id}"):
                        action["type"] = "delete_chat"
                        action["chat_id"] = chat_id
                        return action

        st.markdown("---")
        st.caption("Kintsugi AI • IVURD")

    return action


def render_welcome_screen() -> None:
    st.markdown(
        """
        <div class="kintsugi-box welcome-card">
            <h2>Start a new email reply chat</h2>
            <p>Paste the email context, request, or message you want to answer.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state() -> None:
    st.markdown(
        """
        <div class="muted-note">
            Examples:
            <br>• Reply politely to a client asking for a delay update
            <br>• Write a professional response to an interview invitation
            <br>• Decline a meeting request respectfully
        </div>
        """,
        unsafe_allow_html=True,
    )





import streamlit.components.v1 as components
import html

def render_chat_messages(messages):
    for i, msg in enumerate(messages):
        role_label = "You" if msg["role"] == "user" else "IVURD"
        role_class = "chat-user" if msg["role"] == "user" else "chat-assistant"

        st.markdown(
            f"""
            <div class="kintsugi-box {role_class}">
                <div class="chat-role">{role_label}</div>
                <div class="chat-content">{msg["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ✅ SAFE COPY BUTTON
        if msg["role"] == "assistant":
            safe_text = html.escape(msg["content"])

            components.html(
                f"""
                <button onclick="navigator.clipboard.writeText('{safe_text}')"
                style="
                    background: #111;
                    color: gold;
                    border: 1px solid gold;
                    padding: 6px 12px;
                    border-radius: 8px;
                    cursor: pointer;
                    margin-bottom: 15px;
                ">
                📋 Copy
                </button>
                """,
                height=50,
            )

def render_message_actions() -> str | None:
    c1, c2, c3 = st.columns([1, 1, 4])

    with c1:
        if st.button("Retry", key="retry_btn"):
            return "retry_last"

    with c2:
        if st.button("Clear", key="clear_btn"):
            return "clear_chat"

    return None