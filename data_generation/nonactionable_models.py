import random

from data_generation.util_models import NonActionablePoint


class MetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "MetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"was great meeting {pronoun}",
            f"had a nice chat with {pronoun}",
            f"had a good catchup with {pronoun}"
        ])
        return MetPoint(
            email_point=point
        )

