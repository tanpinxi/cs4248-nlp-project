from abc import abstractmethod

from pydantic import BaseModel


class BasePoint(BaseModel):
    """
    email_point is the string that goes into the language model to generate the email
    randomize this as much as possible, either through random information, or random wording/phrasing

    for all points, keep first character lower case, for easier formatting

    for actionable points, start with a verb instructing the recipient.
    during prompt constructions, a prefix "ask him/her to" will be added to all of these points

    for nonactionable points, start with a verb instructing the language model what to write in the email

    see example in bloom_inference.py for more info
    """
    email_point: str
    is_actionable: bool

    @staticmethod
    @abstractmethod
    def init_point(is_male: bool) -> "BasePoint":
        ...


class ActionablePoint(BasePoint):
    """
    summarized_point is the string that goes into the dataset (as the output)
    do not randomize this, only add the same information that appeared in email_point
    """
    summarized_point: str
    is_actionable: bool = True

    @staticmethod
    @abstractmethod
    def init_point(is_male: bool) -> "ActionablePoint":
        # is_male: True if recipient is male, else False
        # Useful is he/she or his/her is used in the point
        ...


class NonActionablePoint(BasePoint):
    is_actionable: bool = False

    @staticmethod
    @abstractmethod
    def init_point(is_male: bool) -> "NonActionablePoint":
        ...
