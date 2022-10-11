import json
import random
from typing import List, Callable, Type, Tuple, Any

from data_generation.actionable_models import *
from data_generation.bloom_inference import get_bloom_output
from data_generation.gpt_inference import get_gpt_output
from data_generation.nonactionable_models import *
from data_generation.util_models import ActionablePoint, NonActionablePoint, BasePoint

data_file = "email_summary_data.jsonl"

all_actionable_points: List[Type[ActionablePoint]] = [
    BookMeetingPoint,
    BookOnlineMeetingPoint,
    PostponeMeetingPoint,
    ConfirmMeetingAgendaPoint,
    ReviewAttachmentPoint,
    CompleteAttachmentPoint,
    ForwardAttachmentPoint,
    RequestExtensionPoint,
    ApproveRequestPoint,
    RequestUpdatePoint,
    RequestResponsePoint,
    FeedbackPoint,
    ClarificationPoint
]

all_nonactionable_points: List[Type[NonActionablePoint]] = [
    PositiveMetPoint,
    NegativeMetPoint,
    PositiveMeetPoint,
    NegativeMeetPoint,
    PositiveCallPoint,
    NegativeCallPoint,
    PositivePlanPoint,
    NegativePlanPoint,
    SoloIntroPoint,
    PositiveReviewPoint,
    NegativeReviewPoint,
    PositiveMailPoint,
    NegativeMailPoint,
    SchoolPoint,
    ThankPoint,
    ApologyPoint       
]

def generate_prompt_and_summary(
        actionable_points: List[ActionablePoint],
        nonactionable_points: List[NonActionablePoint],
        sender_is_male: bool,
        recipient_is_male: bool
) -> Tuple[str, str]:
    recipient_pronoun = "him" if recipient_is_male else "her"
    points: List[BasePoint] = []
    points.extend(actionable_points)
    points.extend(nonactionable_points)
    random.shuffle(points)
    point_strings = [
        f"- ask {recipient_pronoun} to {x.email_point}"
        if isinstance(x, ActionablePoint)
        else "- " + x.email_point
        for x in points
    ]
    points_block = "\n".join(point_strings)
    tone = random.choice(["friendly and casual", "formal and respectful", "excited and energetic", "rude and annoyed"])
    prompt = f"""Write an email elaborating on all of the following points. 
Sender: {get_random_first_name(sender_is_male)}
Receiver: {get_random_first_name(recipient_is_male)}, a colleague at work
{points_block}
Rephrase the above points to sound natural. To not list them in point form. Write the email in a {tone} tone.

Email:
"""
    summarized_points = (
        "\n".join(["- " + x.summarized_point for x in points if isinstance(x, ActionablePoint)])
        if len(points) > 0
        else "NONE"
    )
    return prompt, summarized_points

def create_email_data(gen_func: Callable[[str], str]) -> Tuple[str, str, str]:
    sender_is_male = bool(random.getrandbits(1))
    recipient_is_male = bool(random.getrandbits(1))
    n_actionable = random.randint(0, 3)
    n_nonactionable = random.randint(2, 5)
    actionable_classes = random.sample(all_actionable_points, k=n_actionable) if n_actionable > 0 else []
    nonactionable_classes = random.sample(all_nonactionable_points, k=n_nonactionable) if n_nonactionable > 0 else []
    actionable_points = [x.init_point(recipient_is_male) for x in actionable_classes]
    nonactionable_points = [x.init_point(recipient_is_male) for x in nonactionable_classes]
    email_prompt, summarized_points = generate_prompt_and_summary(
        actionable_points=actionable_points,
        nonactionable_points=nonactionable_points,
        sender_is_male=sender_is_male,
        recipient_is_male=recipient_is_male,
    )
    email = gen_func(email_prompt)
    return email_prompt, email, summarized_points

def save_data(f_out, email_prompt: str, email: str, summarized_points: str):
    data = {
        "email_prompt": email_prompt,
        "email": email,
        "summary": summarized_points,
    }
    json.dump(data, f_out)
    f_out.write("\n")

def run(n: int, gen_func: Callable[[str], str]):
    f_out = open(data_file, "a+")
    for i in range(n):
        if i % 10 == 0:
            print(i)
        email_prompt, email, summarized_points = create_email_data(gen_func=gen_func)
        save_data(f_out=f_out, email_prompt=email_prompt, email=email, summarized_points=summarized_points)
    f_out.close()

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
    print("Generating data...")
    run(n=num_data, gen_func=gen_func)
