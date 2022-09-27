from abc import abstractmethod

from pydantic import BaseModel


class BasePoint(BaseModel):
    email_point: str  # string that goes into generating the email
    is_actionable: bool

    @staticmethod
    @abstractmethod
    def init_point(is_male: bool) -> "BasePoint":
        ...


class ActionablePoint(BaseModel):
    summarized_point: str  # string that goes into the dataset (as the output)
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
