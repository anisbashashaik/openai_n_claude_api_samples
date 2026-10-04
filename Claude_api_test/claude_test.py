from anthropic import Anthropic
import os
from dotenv import load_dotenv

def ask_claude(question: str):
    
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = Anthropic(api_key=api_key)
    my_message = [{"role": "user", "content": question}]
    response = client.messages.create(
        messages=my_message,
        max_tokens=100,
        model="claude-haiku-4-5")

    process_response(response)

def process_response(response):
    print(f"Output From model: {response.content[-1].text}")
    print(f"Input Tokens: {response.usage.input_tokens}")
    print(f"Output Tokens: {response.usage.output_tokens}")