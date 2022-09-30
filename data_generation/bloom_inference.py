from huggingface_hub.inference_api import InferenceApi

from data_generation.settings import BLOOM_API_KEY


def get_bloom_output(prompt: str) -> str:
    inference = InferenceApi(repo_id="bigscience/bloom", token=BLOOM_API_KEY)
    res = inference(prompt, params={"max_new_tokens": 150, "temperature": 0.6, "return_full_text": False})
    return res[0]["generated_text"].strip()


if __name__ == "__main__":
    prompt = """Write an email elaborating on all of the following points. 
Sender: Paul, the Head of IT
Receiver: John, a colleague at work
- thank him for the call this afternoon
- say you are more familiar with the restructuring planned for next Quarter
Ask him to do the following:
- book a meeting at 4pm next Wednesday
- review the attached legal contract by tomorrow
Rephrase the above points to sound natural. To not list them in point form.
===
Email:
"""
    output = get_bloom_output(prompt)
    print(output)
