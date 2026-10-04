from dotenv import load_dotenv
import os, asyncio
from claude_agent_sdk import query,ClaudeAgentOptions
from helper import base_options, parse_message
from typing import Literal

TONE_DICT = {
    'DETAILED': """You are a tutor, Explain the question asked in a 
    direct fashion. Ensure you add some examples to answer the question""",
    'REVISION': """ You are a tutor, The question asked is before an exam, 
    Help in quickly revising to recollect the learnt topic and give simple, 
    crisp and necessary stuff.
    """,
    'BEGINNER': """You are a tutor, The question asked by the student who has
    zero or minimal conceptual knowledge. Dont make assumptions, Answer the question
    in a elaborate fashion right from concepts required to answer the question.
    """
}

async def initiate_conversation(question: str, tone: Literal['DETAILED', 'REVISION', 'BEGINNER']):
    chosen_tone = TONE_DICT.get(tone, TONE_DICT['BEGINNER'])
    print(f"Chosen tone: {chosen_tone}")
    custom_options = {
        'system_prompt': chosen_tone
    }
    options = base_options(**custom_options)
    count = 0
    async for message in query(prompt=question, options=options):
        count += 1
        print(f"{count}:  {type(message)}")
        parse_message(message=message)
        # Print Output to external File agent_demo_output.md
        with open("agent_demo_output.md", "a", encoding="utf-8") as f:
            f.write(f"{count}: {parse_message(message=message)}\n")

async def ask_question():
    question = input("Enter your question: ")
    tone = input("Enter the tone (DETAILED, REVISION, BEGINNER): ").upper()
    await initiate_conversation(question, tone)
if __name__ == "__main__":
    load_dotenv()
    asyncio.run(ask_question())