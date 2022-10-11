from huggingface_hub.inference_api import InferenceApi

from settings import HUGGINGFACE_API_KEY


def get_bloom_output(prompt: str) -> str:
    inference = InferenceApi(repo_id="bigscience/bloom", token=HUGGINGFACE_API_KEY)
    res = inference(prompt, params={"max_new_tokens": 150, "temperature": 0.6, "return_full_text": False})
    return res[0]["generated_text"].strip()


if __name__ == "__main__":
    prompt = """Write an email elaborating on all of the following points. 
Sender: Paul, the Head of IT
Receiver: John, a colleague at work
- thank him for the call this afternoon
- ask him to review the attached legal contract by tomorrow
- say you are more familiar with the restructuring planned for next Quarter
- ask him to book a meeting at 4pm next Wednesday
Rephrase the above points to sound natural. To not list them in point form.
===
Email:
"""
    output = get_bloom_output(prompt)
    print(output)
