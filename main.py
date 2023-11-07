import json
import os
from typing import Literal

from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, conint, constr, conlist

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class Character(BaseModel):
    full_name: str
    profession: Literal["Wizard", "Fighter", "Cleric", "Rogue"]
    race: Literal["Human", "Goblin", "Fairy"]
    level: conint(ge=1, le=20)
    damage_types: conlist(item_type=Literal["Arcane", "Physical", "Holy", "Shadow"], min_length=1, max_length=3)


user_prompt = """Create a list of 3 characters for a high-fantasy RPG game. 
Follow this Pydantic specification for output:

class Character(BaseModel):
    full_name: str
    profession: Literal["Wizard", "Fighter", "Cleric", "Rogue"]
    race: Literal["Human", "Goblin", "Fairy"]
    level: conint(ge=1, le=20)
    damage_types: conlist(item_type=Literal["Arcane", "Physical", "Holy", "Shadow"], min_length=1, max_length=3)
"""

chat_completion, *_ = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Please output valid JSON"},
        {"role": "user", "content": user_prompt}],
    model="gpt-4-1106-preview",
    response_format={"type": "json_object"},
    temperature=0.2,
).choices
content = chat_completion.message.content
reply = json.loads(content)
print(content)
