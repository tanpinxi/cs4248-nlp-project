import time

from huggingface_hub.inference_api import InferenceApi

from settings import HUGGINGFACE_API_KEY


def get_bloom_output(prompt: str, end_char: str = "===") -> str:
    inference = InferenceApi(repo_id="bigscience/bloom", token=HUGGINGFACE_API_KEY)
    res = inference(
        prompt,
        params={"max_new_tokens": 150, "temperature": 0.6, "return_full_text": False},
    )
    try:
        output = res[0]["generated_text"].strip()
    except KeyError:
        print("Error from Bloom")
        print(res)
        print("Retrying in 1 min...")
        time.sleep(62)
        return get_bloom_output(prompt=prompt, end_char=end_char)
    output = output[len(prompt) :]
    end_idx = output.find(end_char)
    return output[:end_idx].strip()


if __name__ == "__main__":
    prompt = """Write an email elaborating on all of the following points. 

===

Sender: Roberto
Receiver: Lee, a colleague at work
- ask him to explain the industry news again
- say that you look forward to working with him in the future
- say you had a hard time on call with him
- say you miss the email from him
- scold him for missing the meeting
Rephrase the above points to sound natural. To not list them in point form. Write the email in a friendly and casual tone.

Email:

Hi Lee,

I hope you're doing well. I was wondering if you could explain the industry news to me again. I'm really looking forward to working with you in the future.

I had a hard time on call with you the other day. I miss getting your emails. Please try to be more responsive in the future.

Take care,

Roberto

===

Write an email elaborating on all of the following points. 
Sender: Sara
Receiver: Janet, a colleague at work
- tell her there is no need for email
- ask her to confirm that tomorrow's meeting agenda is about annual budget
- ask her to endorse Trisha's request to go on childcare leave
- ask her to clarify the topic again
- scold her for giving you a hard time
Rephrase the above points to sound natural. To not list them in point form. Write the email in a rude and annoyed tone.

Email:

Hey Janet,

I'm getting a little sick of all these emails. Can we just rely on face-to-face communication for once?

Also, can you confirm that tomorrow's meeting is going to be about the annual budget? I don't want to waste my time if it's not.

And while we're at it, can you endorse Trisha's request for childcare leave? I don't see why you're giving her a hard time.

Clarify the topic again? Are you kidding me? I think you need to stop emailing me and actually talk to me in person.

Seriously, Janet. This is getting ridiculous. Stop emailing me and talk to me face-to-face.

Sara

===

Sender: Paul, the Head of IT
Receiver: John, a colleague at work
- thank him for the call this afternoon
- ask him to review the attached legal contract by tomorrow
- say you are more familiar with the restructuring planned for next Quarter
- ask him to book a meeting at 4pm next Wednesday
Rephrase the above points to sound natural. To not list them in point form. Write the email in a friendly tone.

Email:
"""
    output = get_bloom_output(prompt)
    print(output)
