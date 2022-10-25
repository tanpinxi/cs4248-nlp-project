import json
from typing import List, Union, Tuple

import openai

from settings import OPENAI_API_KEY

def get_gpt_logprobs(input: str, model: str) -> Tuple[float, int]:
    res = openai.Completion.create(
        model=model,
        prompt=input,
        max_tokens=0,
        temperature=0,
        stop=[""],
    )
    res_dict = res["choices"][0]

    maybe_logprobs: List[Union[float, None]] = res_dict["logprobs"]["token_logprobs"]
    logprobs: List[float] = [x or 0.0 for x in maybe_logprobs]
    tokens: List[str] = res_dict["logprobs"]["tokens"]
    offsets: List[int] = res_dict["logprobs"]["text_offset"]

    prompt_offset = len(input)
    completion_tokens = 0
    completion_logprob = 0.0
    for i in range(len(tokens) - 1, -1, -1):
        if tokens[i] != "END" and offsets[i] >= prompt_offset:
            completion_tokens += 1
            completion_logprob += logprobs[i]
        elif offsets[i] < prompt_offset:
            break
    return completion_logprob, completion_tokens

def calc_gpt_logprobs(data: List[str], model: str) -> float:
    running_average_logprob = 0.0
    for x in data:
        logprob, tokens = get_gpt_logprobs(x, model)
        running_average_logprob += logprob / tokens
    return running_average_logprob / len(data)

def create_prompt(email: str, summary: str) -> str:
    return email.strip() + "\n\n===\n\n" + summary.strip() + "\nEND"

if __name__ == "__main__":
    openai.api_key = OPENAI_API_KEY
    model_names = [
        "ada:ft-personal:cs4248-2022-10-15-05-02-44",
        "babbage:ft-personal:cs4248-2022-10-15-06-31-30",
        "curie:ft-personal:cs4248-2022-10-15-07-01-21",
    ]

    with open("data/handwritten_data.jsonl", "r") as f:
        json_data = list(map(json.loads, f))
    data = [create_prompt(email=x["email"], summary=x["summary"]) for x in json_data]

    for model in model_names:
        logprob = calc_gpt_logprobs(data=data, model=model)
        print("========")
        print(model)
        print("Average Log Prob:", round(logprob, 6))
