import random

from data_generation.random_generators import get_random_room, get_random_time
from data_generation.util_models import ActionablePoint


class BookMeetingPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "BookMeetingPoint":
        action = random.choice(["schedule", "book", "plan"])
        location = random.choice([f" in {get_random_room()}", ""])
        time = get_random_time()
        email_point = random.choice([
            f"{action} a meeting{location} at {time}",
        ])
        summarized_point = f"book a meeting{location} at {time}"
        return BookMeetingPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )
