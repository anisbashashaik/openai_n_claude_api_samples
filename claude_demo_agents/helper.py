from claude_agent_sdk import (
    ClaudeAgentOptions,
    Message,
    AssistantMessage,
    UserMessage,
    SystemMessage,
    ResultMessage
)

from claude_agent_sdk.types import TextBlock

MODEL_NAME = 'claude-haiku-4-5'

def base_options(**arguments) -> ClaudeAgentOptions:
    settings = {
        'model' : MODEL_NAME,
        'max_turns' : 3
    }
    settings.update(arguments)

    return ClaudeAgentOptions(**settings)

def parse_message(message: Message):
    if isinstance(message, SystemMessage):
        print(f"[System] subtype: {message.subtype}")

    elif isinstance(message, AssistantMessage):
        print("[Assistant Response]")
        for block in message.content:
            if isinstance(block, TextBlock):
                # Add indentation and separators for readability
                print("─" * 40)
                print(block.text.strip())
                print("─" * 40)

    elif isinstance(message, ResultMessage):
        print("[Result]")
        print(f"Duration: {message.duration_ms} ms")
        print(f"Cost: ${message.total_cost_usd:.4f}")
