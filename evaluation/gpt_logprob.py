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

def calc_gpt_logprobs(data: List[str], model: str) -> Tuple[float, int]:
    total_logprob = 0.0
    total_tokens = 0
    for x in data:
        logprob, tokens = get_gpt_logprobs(x, model)
        total_logprob += logprob
        total_tokens += tokens
    return total_logprob, total_tokens

if __name__ == "__main__":
    openai.api_key = OPENAI_API_KEY
    model_names = [
        "ada:ft-personal:cs4248-2022-10-15-05-02-44",
        "babbage:ft-personal:cs4248-2022-10-15-06-31-30",
        "curie:ft-personal:cs4248-2022-10-15-07-01-21",
    ]

    data = ...

    for model in model_names:
        logprob, tokens = calc_gpt_logprobs(data=data, model=model)
        print("========")
        print(model)
        print("Total Log Prob:", round(logprob, 6))
        print("Average Log Prob:", round(logprob / tokens, 6))
