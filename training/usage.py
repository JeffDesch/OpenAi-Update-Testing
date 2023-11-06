import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion, *_ = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Respond with the etymology of the following word"},
        {"role": "user", "content": "Illustration"},
    ],
    model="ft:gpt-3.5-turbo-0613:personal:etymology-bot:8Hz90FDE",
).choices
reply = chat_completion.message.content
print(reply)
