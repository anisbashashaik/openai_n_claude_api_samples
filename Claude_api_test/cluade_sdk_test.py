import os
import asyncio
from anthropic import Anthropic
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions
from claude_agent_sdk.types import AssistantMessage, ResultMessage, TextBlock
from httpx2 import options

async def run_query(question: str):

    options = ClaudeAgentOptions(
        cli_path="C:\\Users\\Anis\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Anthropic.ClaudeCode_Microsoft.Winget.Source_8wekyb3d8bbwe\\claude.exe",
        model="claude-haiku-4-5"
    )
    async for message in  query(prompt=question, options=options) :
        print(f"type: {type(message)}")
        if isinstance(message, ResultMessage):
            print(f"cost {message.total_cost_usd}")
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(f"response: {block.text}")
        

if __name__ == "__main__":
    load_dotenv()
    print("Cluade SDK Test Started")
    question = input("Enter your question for Claude: ")
    response = asyncio.run(run_query(question))
    print(f"Response: {response}")