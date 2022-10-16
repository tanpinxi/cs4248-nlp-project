from huggingface_hub.inference_api import InferenceApi

from settings import HUGGINGFACE_API_KEY


def get_bloom_output(prompt: str) -> str:
    inference = InferenceApi(repo_id="bigscience/bloom", token=HUGGINGFACE_API_KEY)
    res = inference(prompt, params={"max_new_tokens": 20, "temperature": 0.1, "return_full_text": False})
    print(res)
    return res[0]["generated_text"].strip()


if __name__ == "__main__":
    prompt = """List what the sender wants the recipient to do in the email.

For example:

===

Email: 

Hi Joan,\n\nI just wanted to say that I expect better results from you in the future. I think you're a great colleague and I enjoyed meeting you. However, I found our recent meeting to be unpleasant. I'm asking that you set up a meeting in conference room 4 at 8am tomorrow.\n\nThanks for your wonderful contribution to the recent negotiation. I'm looking forward to hearing your recommendations.\n\nBest,\n\nDavid

List to do:
- book a meeting at 8 am for tomorrow
- give feedback

===

Email:

Hi Holly,\n\nCan you please check if today's sharing agenda is about progress on quarterly goals? I didn't attend the previous meeting, but I expect better results from you in the future.\n\nThe plan is going to fail if we don't get better results. Thank you for not ignoring me.\n\nSincerely,\n\nBrenda

List to do:
- confirm that today's meeting agenda is about progress on quarterly goals

===

Email:

Hey John,

Great getting to know you and your team. I'm excited to be part of this amazing department and look forward to working with you!

In the meantime, could you take a look at the minutes of the budget review discussed today? I'd need to know by Thursday if that's possible.

Also, could you share any progress you have had on the marketing review? I will be sharing it with the management team later. Also will need you to setup a Zoom call tomorrow 2pm with the CFO for this sharing. 

Thanks.
Peter

List to do:
"""
    output = get_bloom_output(prompt)
    print(output)
