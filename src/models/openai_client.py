import openai
from src.config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE, SYSTEM_PROMPT

class OpenAIClient:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.model = MODEL_NAME
        self.max_tokens = MAX_TOKENS
        self.temperature = TEMPERATURE
        self.system_prompt = SYSTEM_PROMPT

    def generate_response(self, user_input: str) -> str:
        """
        Generate a response using OpenAI's API.
        
        Args:
            user_input (str): The user's input message
            
        Returns:
            str: The generated response
        """
        try:
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"