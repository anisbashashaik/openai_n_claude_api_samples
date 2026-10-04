
import os
from dotenv import load_dotenv
from anthropic import Anthropic


def get_weather(city: str) -> dict:

    fake_weather_db = {
        "Hyderabad": {"temperature": "30°C", "condition": "Sunny"},
        "Bangalore": {"temperature": "25°C", "condition": "Rainy"},
        "Chennai": {"temperature": "32°C", "condition": "Cloudy"},
        "Mumbai": {"temperature": "28°C", "condition": "Windy"}
    }
    return fake_weather_db.get(city, {"temperature": "N/A", "condition": "Weather data not available"})

def ask_claude_to_get_weather_using_tool(question: str):
    
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = Anthropic(api_key=api_key)

    tools_definition = [{
        "name": "get_weather",
        "description": "Retrieves the current temperature, weather forecast, and climate details for a specified city.",
        "input_schema": {
            "type": "object",
            "properties": {
            "city": {
                "type": "string",
                "description": "The name of the city to look up the weather for, e.g., 'hyderabad' or 'bangalore'."
            }
            },
            "required": ["city"]
        }
    }]
    
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

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        print("ANTHROPIC_API_KEY loaded successfully.")
        ask_claude_to_get_weather_using_tool("What is the weather in Hyderabad")
    else:
        print("Failed to load ANTHROPIC_API_KEY.")

