import streamlit as st
from src.models.openai_client import OpenAIClient
from src.utils.chat_utils import (
    initialize_chat_history,
    add_message,
    display_chat_messages
)
from src.config import EMERGENCY_RESOURCES

def setup_page():
    """Configure the Streamlit page settings."""
    st.set_page_config(
        page_title="Mental Health Support Chatbot",
        page_icon="��",
        layout="wide"
    )

def display_header():
    """Display the app header and description."""
    st.title("🧠 Mental Health Support Chatbot")
    st.markdown("""
    This chatbot is designed to:
    - Help you assess your symptoms
    - Provide non-medical advice and support
    - Offer general wellness tips
    - Suggest when to seek professional help

    **Note:** This is not a replacement for professional medical advice. 
    Always consult with healthcare providers for medical concerns.
    """)

def display_sidebar():
    """Display the sidebar with additional information."""
    with st.sidebar:
        st.markdown("### About")
        st.markdown("""
        This chatbot uses AI to provide mental health support and guidance. 
        Remember:
        - This is not medical advice
        - Always consult professionals for serious concerns
        - Your privacy is important
        """)
        
        st.markdown("### Emergency Resources")
        st.markdown(f"""
        If you're experiencing a mental health emergency:
        - Call emergency services: {EMERGENCY_RESOURCES['emergency_services']}
        - National Suicide Prevention Lifeline: {EMERGENCY_RESOURCES['suicide_prevention']}
        - Crisis Text Line: Text HOME to {EMERGENCY_RESOURCES['crisis_text_line']}
        """)

def main():
    """Main application function."""
    # Setup
    setup_page()
    initialize_chat_history()
    openai_client = OpenAIClient()
    
    # Display UI elements
    display_header()
    st.markdown("### Chat with the Assistant")
    display_chat_messages()
    display_sidebar()
    
    # Chat input and response
    if prompt := st.chat_input("How are you feeling today?"):
        # Handle user input
        add_message("user", prompt)
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display response
        with st.chat_message("assistant"):
            response = openai_client.generate_response(prompt)
            st.markdown(response)
            add_message("assistant", response)

if __name__ == "__main__":
    main()