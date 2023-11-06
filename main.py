import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion, *_ = client.chat.completions.create(
    messages=[{"role": "user", "content": "Say this is a test"}],
    model="gpt-3.5-turbo",
).choices
reply = chat_completion.message.content
print(reply)
