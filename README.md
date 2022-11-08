# cs4248-nlp-project

## Overview

This project consists of a language model which extracts a list of actionable points from a given email. 
The language model is trained on an original dataset generated using data inversion.
Self-crafted actionable points and non-actionable points are used with pretrained language models to generate the dataset.
The language model is then evaluated with our handwritten dataset.

## How to run

### 1. Setup

Install the dependencies in requirements.txt found inside the repository.

### 2. Generate data

Run the python file data_generation/data_generator.py found inside the data_generation folder. <br/>
The generated data is saved under data/gpt_generated_data.jsonl and data/bloom_generated_data.jsonl and is used for training. <br/>
The handwritten data is under data/handwritten_data.jsonl and is used for evaluation.

### 3. Finetune bloom

Run the Jupyter Notebook finetuning/bloom_finetune.ipynb found inside the finetuning folder.

### 4. Run evaluation script

Run the Jupyter Notebook evaluation/bloom_loss.ipynb found inside the evaluation folder.