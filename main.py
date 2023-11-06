import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

user_prompt = """Create a character for an RPG game, choose a name, class, age, level, and finally write a short visual description.
Follow this example:

{
    "name": <name>, 
    "class": <class>, 
    "age": <age>, 
    "level": <level>, 
    "description": <description>
}
"""
chat_completion, *_ = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Please output valid JSON"},
        {"role": "user", "content": user_prompt}],
    model="gpt-4-1106-preview",
    response_format={"type": "json_object"},
).choices
content = chat_completion.message.content
print(content)
reply = json.loads(content)
print(reply)
