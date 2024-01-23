import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv()

# openai.api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI()
model = "gpt-4"

#== Create our Assistant ==

personal_trainer_assis = client.beta.assistants.create(
    name="Personal Trainer",
    instructions="""You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles.
    You have trained high-caliber atheletes and movie stars.""",
    model=model
)
assistant_id=personal_trainer_assis.id
print(assistant_id)

#=== Thread ===

thread = client.beta.threads.create(
    messages=[
        {
           "role": "user",
           "content": "How do I get started working out to lose fat and build muscles?"
        }
    ]
)
thread_id = thread.id
print(thread_id)