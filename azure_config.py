import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class AzureConfig:
    API_TYPE = os.getenv("AZURE_OPENAI_API_TYPE", "azure")
    API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
    API_BASE = os.getenv("AZURE_OPENAI_API_BASE", "")
    API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    ENGINE = os.getenv("AZURE_OPENAI_ENGINE", "")

# Ensure API key is set
if not AzureConfig.API_KEY:
    raise ValueError("Azure OpenAI API key is missing! Check your .env file.")
