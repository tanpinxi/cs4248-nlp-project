import random
from abc import abstractmethod

from pydantic import BaseModel

from data_generation.random_util import get_random_time, get_random_room


class BasePoint(BaseModel):
    email_point: str
    summarized_point: str
    is_actionable: bool

    @staticmethod
    @abstractmethod
    def init_point() -> "BasePoint":
        ...


class BookMeetingPoint(BasePoint):

    @staticmethod
    def init_point() -> "BookMeetingPoint":
        action = random.choice(["Schedule", "Book", "Plan"])
        location = random.choice([f" in {get_random_room()}", ""])
        time = get_random_time()
        email_point = random.choice([
            f"{action} a meeting{location} at {time}",
        ])
        summarized_point = f"Book a meeting{location} at {time}"
        return BookMeetingPoint(
            email_point=email_point,
            summarized_point=summarized_point,
            is_actionable=True,
        )


if __name__ == "__main__":
    print(BookMeetingPoint.init_point())
