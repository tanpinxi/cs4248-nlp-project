import requests

from settings import HUGGINGFACE_API_KEY


API_URL = "https://api-inference.huggingface.co/models/bigscience/T0pp"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}


def get_t0pp_output(prompt: str) -> str:
    query = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=query)
    return response.json()


if __name__ == "__main__":
    prompt = """Write an email elaborating on all of the following points. 
Sender: Paul, the Head of IT
Receiver: John, a colleague at work
- thank him for the call this afternoon
- say you are more familiar with the restructuring planned for next Quarter
- ask him to book a meeting at 4pm next Wednesday
- ask him to review the attached legal contract by tomorrow
Rephrase the above points to sound natural. To not list them in point form.
===
Email:
"""
    output = get_t0pp_output(prompt)
    print(output)
