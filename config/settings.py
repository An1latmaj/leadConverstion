import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure OpenAI Configuration
AZURE_OPENAI_CONFIG = {
    "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview"),
    "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.getenv("AZURE_OPENAI_KEY"),
    "deployment": os.getenv("AZURE_OPENAI_DEPLOYMENT", "o4-mini")
}

# Application Settings
APP_CONFIG = {
    "title": "AI Career Quiz - Discover Your Perfect Career Match",
    "description": "Professional career consultation powered by AI",
    "version": "1.0.0"
}
