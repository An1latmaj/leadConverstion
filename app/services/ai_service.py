from openai import AzureOpenAI
from typing import List, Dict
from config.settings import AZURE_OPENAI_CONFIG

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_version=AZURE_OPENAI_CONFIG["api_version"],
    azure_endpoint=AZURE_OPENAI_CONFIG["azure_endpoint"],
    api_key=AZURE_OPENAI_CONFIG["api_key"]
)

class AIService:
    @staticmethod
    async def generate_career_preview(prompt: str) -> str:
        """Generate career preview analysis"""
        messages = [
            {"role": "system", "content": (
                "You are an expert career coach creating short, high-converting previews for a career quiz. "
                "Given quiz answers and excluded careers, respond in under 120 words with: \n"
                "1. A bold, attention-grabbing headline for the top career match\n"
                "2. A one-line teaser for 2 other promising careers\n"
                "3. A curiosity-driven hint of a surprising career twist\n"
                "4. A one-line call-to-action encouraging full report access."
            )},
            {"role": "user", "content": prompt}
        ]

        response = await client.chat.completions.create(
            model=AZURE_OPENAI_CONFIG["deployment"],
            messages=messages,
            temperature=0.7,
            max_completion_tokens=250
        )

        return response.choices[0].message.content

    @staticmethod
    async def chat_with_ai(messages: List[Dict[str, str]]) -> str:
        """Handle chat conversations with memory"""
        response = await client.chat.completions.create(
            model=AZURE_OPENAI_CONFIG["deployment"],
            messages=messages,
            temperature=0.7,
            max_completion_tokens=500
        )
        return response.choices[0].message.content
