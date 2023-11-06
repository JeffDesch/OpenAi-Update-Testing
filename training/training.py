import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

with open("training.jsonl", "rb") as file:
    result = client.files.create(file=file, purpose="fine-tune")
print(result.id)
# file-3ZT8re7tL3lZ8znsBPhs7e5B
