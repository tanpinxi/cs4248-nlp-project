from abc import abstractmethod

from pydantic import BaseModel


class BasePoint(BaseModel):
    # string that goes into generating the email
    # for actionable points, start with a verb instructing the recipient
    # for nonactionable points, start with a verb instructing the language model
    # keep first character lower case, for easier formatting
    # see example in bloom_inference.py for more info
    email_point: str
    is_actionable: bool

    @staticmethod
    @abstractmethod
    def init_point(is_male: bool) -> "BasePoint":
        ...


class ActionablePoint(BaseModel):
    # string that goes into the dataset (as the output)
    summarized_point: str
    is_actionable: bool = True

    @staticmethod
    @abstractmethod
    def init_point(is_male: bool) -> "ActionablePoint":
        # is_male: True if recipient is male, else False
        # Useful is he/she or his/her is used in the point
        ...


class NonActionablePoint(BaseModel):
    is_actionable: bool = False

    @staticmethod
    @abstractmethod
    def init_point(is_male: bool) -> "ActionablePoint":
        ...
