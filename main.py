import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

user_prompt = """Create a list of 3 characters for a high-fantasy RPG game. 
Higher level characters should have very epic gear and titles compared to lower level characters' junk gear. 
Characters approaching level 20 should have many unique and powerful items. 
Follow this specification:
{
    fullname: {type: String, description: The character's full name, two to five words in length.},
    nickname: {type: String, description: Nickname used by friends and family.},
    title: Optional[String],
    class: Literal[Wizard, Fighter, Cleric],
    race: Literal[Human, Dwarf, Elf],
    gender: Literal[Female, Male, Non-binary],
    age: Float,
    level: Integer[1, 20],
    description: {type: String, description: Three to five sentences describing the visual appearance of the character.},
    damage_types: List[Literal[Fire, Frost, Arcane, Slashing, Piecing, Bludgeoning, Holy, Void]],
    weapons: {type: List[String], count: Range(0, 2)},
    armor: {type: List[String], count: Range(0, 2)},
    jewelry: {type: List[String], count: Range(0, 2)} 
}"""

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
