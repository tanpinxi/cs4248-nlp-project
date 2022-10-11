import json
import random
from datetime import datetime
from pathlib import Path
from typing import List

import neptune.new

from settings import NEPTUNE_KEY
from finetuning.finetune_openai import start_finetune_job, await_finetune_job, get_finetune_results
from finetuning.models import PromptCompletion, FineTuneParams, ModelId


def write_training_data(
    training_data: List[PromptCompletion],
    output: Path,
):
    with open(output, "w") as f:
        for item in training_data:
            # exclude_none is needed because some prompts have None as weights
            f.write(json.dumps(item.dict()) + "\n")

def finetune_with_neptune_logging(
    train_data: List[PromptCompletion],
    params: FineTuneParams,
    project_name: str,
) -> ModelId:
    # Take and train from a sample of the dataset
    print(f"Finetuning on {len(train_data)} examples...")
    random.shuffle(train_data)

    now = datetime.now()
    timestamp = str(int(datetime.now().timestamp()))
    file_path = Path.cwd() / Path(
        "train" + now.strftime("%Y-%m-%d") + f"_{timestamp}.jsonl"
    )
    write_training_data(
        train_data,
        output=file_path,
    )

    should_continue = False
    while should_continue is not True:
        user_input = input(
            f"Wrote training data to {file_path}. Please check if the data is valid. [continue/abort]\n"
        )
        if user_input == "continue":
            should_continue = True
        elif user_input == "abort":
            raise RuntimeError("Aborted fine tuning")
        else:
            print("Invalid input")

    try:
        run = neptune.new.init(
            project=f"leadiq/{project_name}",
            api_token=NEPTUNE_KEY,
        )

        # Add dataset to neptune
        run["train_data"].upload(str(file_path))
        run["num_data"] = len(train_data)
        # Add params to neptune
        run["parameters"] = params.dict()

        # Set suffix as project_name
        params.project_suffix = project_name
        job_id = start_finetune_job(train_path=file_path, params=params)
        run["job_id"] = job_id

        model_id = await_finetune_job(job_id)
        print("Finetune succeeded!")
        print(f"Finetuned model: {model_id}")
        run["model_id"] = model_id

        result = get_finetune_results(job_id)
        # Add metrics to draw charts
        for item in result.metrics:
            for k, v in item.dict().items():
                run[k].log(v)

        run["events"] = result.events.map(lambda x: x.dict())
        run["cost"] = (
            result.events.map(lambda x: x.extract_cost()).flatten_option().first_option
        )
        run["final_parameters"] = result.final_params
        return model_id

    finally:
        print("Access run information at", run.get_run_url())
        run.stop()
