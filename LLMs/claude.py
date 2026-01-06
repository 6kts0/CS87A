"""
Initialize a .env file to hold your API key
"""

from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

client = anthropic.Anthropic()

user_prompt = input("Enter a city: ")

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": f"Give me a summary of the current weather in {user_prompt.strip().title()}. Condense your output response to less than or equal to 200 words."
        }
    ]
)

print(message.content)

