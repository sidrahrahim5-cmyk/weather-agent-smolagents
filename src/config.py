import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# HuggingFace Token
HF_TOKEN = os.getenv("HF_TOKEN")

# Model Settings
MODEL_ID = "Qwen/Qwen2.5-72B-Instruct"

# App Settings
APP_TITLE = "🌤️ AI Weather Agent"
APP_DESCRIPTION = """
### Powered by Smolagents & HuggingFace
Ask me about weather in any city around the world!
"""

# Weather Tool Settings
WEATHER_TIMEOUT = 10  # seconds