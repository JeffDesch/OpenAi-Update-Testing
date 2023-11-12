import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    organization=os.environ.get("OPENAI_ORG_KEY"),
)

models = client.models.list()
output = [model for model in models if "gpt" in model.id]
print(*output, sep="\n")
