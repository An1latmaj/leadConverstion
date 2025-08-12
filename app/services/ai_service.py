from openai import AzureOpenAI
from typing import List, Dict
from config.settings import AZURE_OPENAI_CONFIG
from app.services.career_matcher import career_matcher

# Initialize Azure OpenAI client with error handling
try:
    client = AzureOpenAI(
        api_version=AZURE_OPENAI_CONFIG["api_version"],
        azure_endpoint=AZURE_OPENAI_CONFIG["azure_endpoint"],
        api_key=AZURE_OPENAI_CONFIG["api_key"]
    )
except Exception as e:
    print(f"Warning: Azure OpenAI client initialization failed: {e}")
    client = None

class AIService:
    @staticmethod
    async def generate_career_preview(prompt: str) -> str:
        """Generate career preview analysis with one revealed career and paywalled content"""
        # Parse the prompt to extract answers and excluded careers
        try:
            # Extract answers and excluded careers from the prompt
            parts = prompt.split(", Exclude: ")
            answers_part = parts[0].replace("Answers: ", "")
            excluded_part = parts[1] if len(parts) > 1 else "[]"

            # Parse the answers (they come as a string representation of a dict)
            import ast
            answers = ast.literal_eval(answers_part)
            excluded_careers = ast.literal_eval(excluded_part) if excluded_part != "[]" else []

            # Use rule-based career matcher
            preview = career_matcher.generate_career_preview(answers, excluded_careers)
            return preview

        except Exception as e:
            print(f"Error parsing quiz data: {e}")
            # Fallback to rule-based system with empty data
            return career_matcher.generate_career_preview({}, [])

    @staticmethod
    async def chat_with_ai(messages: List[Dict[str, str]]) -> str:
        """Handle chat conversations with memory"""
        if not client:
            return "AI chat service is currently unavailable. Please try again later."

        try:
            response = client.chat.completions.create(
                model=AZURE_OPENAI_CONFIG["deployment"],
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI chat temporarily unavailable: {str(e)}"
