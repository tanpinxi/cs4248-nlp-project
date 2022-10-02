import random

from data_generation.random_generators import get_random_room, get_random_time, get_random_day, get_random_meeting_platform
from data_generation.util_models import ActionablePoint

# Scheduling 
class BookMeetingPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "BookMeetingPoint":
        action = random.choice(["schedule", "book", "plan", "arrange", "set up"])
        location = random.choice([f" in {get_random_room()}", ""])
        day = random.choice([f"next {get_random_day()}",  f"this {get_random_day()}", "tomorrow"])
        time = get_random_time()
        email_point = random.choice([
            f"{action} a meeting{location} at {time} for {day}",
        ])
        summarized_point = f"book a meeting{location} at {time} for {day}"
        return BookMeetingPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )

class BookOnlineMeetingPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "BookOnlineMeetingPoint":
        action = random.choice(["schedule", "book", "plan", "arrange", "set up"])
        platform = random.choice([f"{get_random_meeting_platform()}"])
        day = random.choice([f"next {get_random_day()}",  f"this {get_random_day()}", "tomorrow"])
        time = get_random_time()
        email_point = random.choice([
            f"{action} a meeting on {platform} at {time} for {day}",
            f"send a {platform} invitation for {day} at {time}",
            f"create a {platform} meeting invite for {day} at {time}"
            f"discuss on {platform} {day} at {time}"
        ])
        summarized_point = f"schedule an online meeting on {platform} at {time} for {day}"
        return BookOnlineMeetingPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )