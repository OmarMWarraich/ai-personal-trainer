import os
import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

load_dotenv()

# openai.api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI()
model = "gpt-4"

#== Create our Assistant ==

# personal_trainer_assis = client.beta.assistants.create(
#     name="Personal Trainer",
#     instructions="""You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles.
#     You have trained high-caliber atheletes and movie stars.""",
#     model=model
# )
# assistant_id=personal_trainer_assis.id
assistant_id = os.environ.get("OPENAI_ASSISTANT_ID")
# print(assistant_id)


#=== Thread ===

# thread = client.beta.threads.create(
#     messages=[
#         {
#            "role": "user",
#            "content": "How do I get started working out to lose fat and build muscles?"
#         }
#     ]
# )
# thread_id = thread.id
thread_id = os.environ.get("OPENAI_THREAD_ID")
# print(thread_id)

# ==== Create a Message ====
# message = "What are the best excercises for lean muscles and getting strong"
message = "How much water do I need to drink in a day to stay hydrated?"

message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

# ===== Run our Assistant =====
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as John Doe"
)

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """

    Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
    :param thread_id: The ID of the thread.
    :param run_id: The ID of the run.
    :param sleep_interval: Time in seconds to wait between checks.
    """
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")
                # Get messages here once Run is completed!
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)


# === Run ===
wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

# ==== Steps --- Logs ==
run_steps = client.beta.threads.runs.steps.list(thread_id=thread_id, run_id=run.id)
print(f"Steps---> {run_steps.data[0]}")

"""
Response 1
Run completed in 00:00:17
Assistant Response: Dear John Doe,

Building lean muscles and gaining strength requires a blend of strength training exercises and cardiovascular workouts. Here are some exercises you might consider:

1. Weight Lifting: Compound movements like squats, deadlifts, bench presses, and overhead presses work multiple muscles simultaneously and are ideal for building lean muscle.

2. Bodyweight Exercises: Push-ups, pull-ups, lunges, squats, and planks are effective exercises that require no equipment. They can be done anywhere, making them very convenient.

3. High-Intensity Interval Training (HIIT): As a potent cardio exercise, HIIT offers substantial calorie burn that can help in fat loss. The intense bursts of activity followed by recovery periods keep your heart rate up and boost your metabolism.

4. Cardio Exercises: Regular cardio exercises like jogging, swimming, biking, or rowing can also build strength and assist in maintaining leanness.

5. Yoga/Pilates: While generally not seen as strength builders, these exercises offer valuable benefits for muscle toning, flexibility, and core strength, contributing to overall fitness and leanness.

Remember to vary your workout routine regularly to avoid plateaus and ensure all your muscle groups are given adequate attention. Lastly, your diet is critical. Make sure to consume sufficient protein for muscle growth and recovery, and maintain a balanced diet with plenty of vegetables, fruits, and whole grains.

I hope you find these tips helpful. Feel free to reach out with any further questions!

Best regards,
[Your Name]
Steps---> RunStep(id='step_kioyLx5adXfHjLBzv6d2WQA2', assistant_id='asst_9ZGe8HVmYJSfakNZazgCeZlv', cancelled_at=None, completed_at=1706002755, created_at=1706002739, expired_at=None, failed_at=None, last_error=None, metadata=None, object='thread.run.step', run_id='run_xz3kmPNek15fyYbbxogwdCyQ', status='completed', step_details=MessageCreationStepDetails(message_creation=MessageCreation(message_id='msg_fetotptJfzB4kguwIolmgFdH'), type='message_creation'), thread_id='thread_RUPtnL9MytJhmRUCeINIp9AL', type='message_creation', usage=Usage(completion_tokens=304, prompt_tokens=258, total_tokens=562), expires_at=None)
"""

"""
Response 2
Run completed in 00:00:13
Assistant Response: Dear John Doe,

Hydration plays a key role in maintaining good health. The amount of water one needs can depend on several factors like age, weight, gender, activity level, and overall health. However, a common guideline often recommended by health professionals is to drink at least eight 8-ounce glasses of water a day, which equals about 2 liters or half a gallon known as the "8x8 rule."

Another widely recommended guideline is drinking at least half of your body weight in ounces each day. For example, if you weigh 150 pounds (around 68 kilograms), you should try to consume at least 75 ounces (around 2.2 liters) of water daily.

Remember that other beverages such as tea and coffee, and high-water foods like fruits and vegetables, also contribute to your hydration status.

Don’t wait until you're thirsty to drink. Thirst can often be mistaken for hunger, leading to overeating, and dehydration can often be mistaken as fatigue. 

Please note, it's possible to drink too much water, which can lead to water toxicity, although it is rare. 

I hope this helps. If you have any further questions, feel free to ask.

Best Regards,
[Your Name]
Steps---> RunStep(id='step_Eopq6NfEa3p5VaRMpb25HAZ3', assistant_id='asst_9ZGe8HVmYJSfakNZazgCeZlv', cancelled_at=None, completed_at=1706002986, created_at=1706002974, expired_at=None, failed_at=None, last_error=None, metadata=None, object='thread.run.step', run_id='run_k9RDrGIqtMLN0G1z9Ywt3mcS', status='completed', step_details=MessageCreationStepDetails(message_creation=MessageCreation(message_id='msg_w2nVRW1yAAnCTfh7ipEeiMGT'), type='message_creation'), thread_id='thread_RUPtnL9MytJhmRUCeINIp9AL', type='message_creation', usage=Usage(completion_tokens=251, prompt_tokens=581, total_tokens=832), expires_at=None)
"""