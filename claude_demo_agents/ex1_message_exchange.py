import os
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio

from helper import base_options, parse_message

async def initiate_conversation(question: str):

    count = 0   
    options = base_options()
    print("Conversation initiated.")
    async for message in query(prompt=question, options=options):
        count += 1
        print(f"Message {count}: {message}")
        parse_message(message=message)

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(initiate_conversation(input("Enter your question:")))