from typing import List, Dict
import streamlit as st

def initialize_chat_history():
    """Initialize the chat history in session state if it doesn't exist."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_message(role: str, content: str):
    """Add a message to the chat history."""
    st.session_state.messages.append({"role": role, "content": content})

def get_chat_history() -> List[Dict[str, str]]:
    """Get the current chat history."""
    return st.session_state.messages

def display_chat_messages():
    """Display all messages in the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])