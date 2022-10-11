from typing import List

import openai
from jsonlines import jsonlines

from settings import OPENAI_API_KEY
from finetuning.finetune_neptune import finetune_with_neptune_logging
from finetuning.models import PromptCompletion, FineTuneParams

data_file_path = "../data/lm_generated_data.jsonl"
openai.api_key = OPENAI_API_KEY

def get_training_data() -> List[PromptCompletion]:
    print(f"Reading data from {data_file_path}...")
    data: List[PromptCompletion] = []
    with jsonlines.open(data_file_path, "r") as reader:
        for item in reader:
            prompt_completion = PromptCompletion(
                prompt=item["email"].strip() + "\n\n===\n\n",
                completion=item["summary"].strip() + "\nEND",
            )
            data.append(prompt_completion)
    print(f"Found {len(data)} data points.")
    return data

if __name__ == "__main__":
    # Finetuning parameters, change if desired
    model_name = "babbage"
    num_epoch = 2
    learning_rate_multiplier = 0.1
    neptune_project = "pinxi-tan/cs4248"

    data = get_training_data()

    finetune_with_neptune_logging(
        train_data=data,
        params=FineTuneParams(
            model=model_name,
            n_epochs=num_epoch,
            learning_rate_multiplier=learning_rate_multiplier
        ),
        project_name=neptune_project,
    )
