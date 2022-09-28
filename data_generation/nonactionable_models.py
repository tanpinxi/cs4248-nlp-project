import random

from data_generation.util_models import NonActionablePoint


class MetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "MetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} it was great meeting {pronoun}",
            f"say you had a nice chat with {pronoun}",
            f"tell {pronoun} you had a good catchup with {pronoun}"
        ])
        return MetPoint(
            email_point=point
        )
