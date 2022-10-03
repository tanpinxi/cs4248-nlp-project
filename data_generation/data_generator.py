import random
from typing import List, Callable, Type, Tuple

from data_generation.actionable_models import *
from data_generation.bloom_inference import get_bloom_output
from data_generation.gpt_inference import get_gpt_output
from data_generation.util_models import ActionablePoint, NonActionablePoint, BasePoint

all_actionable_points: List[Type[ActionablePoint]] = [
    BookMeetingPoint,
    BookOnlineMeetingPoint,
    PostponeMeetingPoint,
    ReviewAttachmentPoint,
    CompleteAttachmentPoint,
    ForwardAttachmentPoint,
]

all_nonactionable_points: List[Type[NonActionablePoint]] = [
    NonActionablePoint,
]

def generate_prompt_and_completion(
        actionable_points: List[ActionablePoint],
        nonactionable_points: List[NonActionablePoint],
        sender_is_male: bool,
        recipient_is_male: bool
) -> Tuple[str, str]:
    recipient_pronoun = "male" if recipient_is_male else "female"
    points: List[BasePoint] = actionable_points + nonactionable_points
    random.shuffle(points)
    point_strings = [f"ask {recipient_pronoun} to {x.email_point}" if isinstance(x, ActionablePoint) else x.email_point for x in actionable_points]
    points_block = "\n- ".join(point_strings)
    prompt = f"""Write an email elaborating on all of the following points. 
Sender: {get_random_first_name(sender_is_male)}
Receiver: {get_random_first_name(recipient_is_male)}, a colleague at work
{points_block}
Rephrase the above points to sound natural. To not list them in point form.

Email:
"""
    completion = "\n- ".join([x.summarized_point for x in points if isinstance(x, ActionablePoint)])
    return prompt, completion

def create_email_data(gen_func: Callable[[str], str]):
    sender_is_male = bool(random.getrandbits(1))
    recipient_is_male = bool(random.getrandbits(1))
    n_actionable = random.randint(0, 3)
    n_nonactionable = random.randint(1, 3)
    actionable_classes = random.sample(all_actionable_points, k=n_actionable) if n_actionable > 0 else []
    nonactionable_classes = random.sample(all_nonactionable_points, k=n_nonactionable) if n_nonactionable > 0 else []
    actionable_points = [x.init_point(recipient_is_male) for x in actionable_classes]
    nonactionable_points = [x.init_point(recipient_is_male) for x in nonactionable_classes]
    prompt, completion = generate_prompt_and_completion(
        actionable_points=actionable_points,
        nonactionable_points=nonactionable_points,
        sender_is_male=sender_is_male,
        recipient_is_male=recipient_is_male,
    )
    email = gen_func(prompt)
    return email, completion

if __name__ == "__main__":
    while True:
        try:
            num_data = int(input("How many data points to generate: "))
            break
        except ValueError:
            print("Enter a valid number.")
    while True:
        gen_method = input("Which LM to generate data with? [bloom/gpt]: ").lower().strip()
        if gen_method == "bloom":
            gen_func = get_bloom_output
            break
        elif gen_method == "gpt":
            gen_func = get_gpt_output
            break
        else:
            print("Enter a valid method.")
