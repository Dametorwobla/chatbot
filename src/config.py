import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration constants
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_NAME = "gpt-3.5-turbo"
MAX_TOKENS = 200
TEMPERATURE = 0.7

# System prompts
SYSTEM_PROMPT = """You are a supportive mental health chatbot. 
Provide helpful, non-medical advice and support. 
Always maintain a compassionate and understanding tone."""

# Emergency resources
EMERGENCY_RESOURCES = {
    "emergency_services": "911",
    "suicide_prevention": "988",
    "crisis_text_line": "741741"
}