import os
from dotenv import load_dotenv
from anthropic import Anthropic

from claude_test import ask_claude

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        print("ANTHROPIC_API_KEY loaded successfully.")
        ask_claude("What is Capital of India")
    else:
        print("Failed to load ANTHROPIC_API_KEY.")