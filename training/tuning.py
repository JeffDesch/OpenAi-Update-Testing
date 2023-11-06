import os
from time import sleep

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

result = client.fine_tuning.jobs.create(
    training_file="file-3ZT8re7tL3lZ8znsBPhs7e5B",
    model="gpt-3.5-turbo",
    suffix="etymology-bot",
)
job_id = result.id
print(job_id)
# ftjob-9dq5xd6xTa3RdCMfAExo1i4M

while True:
    sleep(60)
    if client.fine_tuning.jobs.retrieve(job_id).status == "running":
        print("Running")
    else:
        break

print(client.fine_tuning.jobs.retrieve(job_id).fine_tuned_model)
# ft:gpt-3.5-turbo-0613:personal:etymology-bot:8Hz90FDE
