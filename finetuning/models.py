import re
from enum import Enum
from typing import Optional, NewType, Dict, List, Any

from pydantic import BaseModel

JobId = NewType("JobId", str)
ModelId = NewType("ModelId", str)

class PromptCompletion(BaseModel):
    prompt: str
    completion: str

class FineTuneParams(BaseModel):
    model: str
    n_epochs: int = 4
    learning_rate_multiplier: float = 0.1
    prompt_loss_weight: float = 0.001
    batch_size: Optional[int] = None
    project_suffix: Optional[str] = None

class FinetuneStates(str, Enum):
    pending = "pending"
    running = "running"
    succeeded = "succeeded"

class FineTuneMetrics(BaseModel):
    step: int
    elapsed_tokens: int
    elapsed_examples: int
    training_loss: float
    training_sequence_accuracy: float
    training_token_accuracy: float

class FineTuneEvent(BaseModel):
    created_at: int
    level: str
    message: str
    object: str

    def extract_cost(self) -> Optional[str]:
        """
        extracts the cost if the message has it,
        typically appears as "Fine-tune costs $38.48"
        """
        match = re.search(r"costs \$(.*)", self.message)
        if match:
            return match.group(1)
        else:
            return None

class FineTuneResult(BaseModel):
    metrics: List[FineTuneMetrics]
    events: List[FineTuneEvent]
    final_params: Dict[Any, Any]
