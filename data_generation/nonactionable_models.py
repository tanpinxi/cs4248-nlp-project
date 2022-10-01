import random

from data_generation.util_models import NonActionablePoint


class MetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "MetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} it was great meeting {pronoun}",
            f"tell {pronoun} you had a good catchup with {pronoun}",
            f"tell {pronoun} you appreciate to have met {pronoun}",
            f"tell {pronoun} you regret meeting {pronoun}",
            f"tell {pronoun} getting to see {pronoun} was a good experience",
            f"tell {pronoun} you now know {pronoun} better",
            f"say you had a nice chat with {pronoun}",
            f"say the conversation with {pronoun} is great",
            f"say you want to keep in touch with {pronoun}",
            f"say the talk with {pronoun} is bad",
            f"say you want to meet {pronoun} again as soon as possible",
            f"say you do not want to meet {pronoun} again",
            f"thank {pronoun} for providing time for you",
            f"thank {pronoun} for not ignoring you",
            f"thank {pronoun} for helping you during the catchup",
            f"scold {pronoun} for being unresponsive",
            f"scold {pronoun} for giving you a hard time",
            f"scold {pronoun} for wasting your time"
        ])
        return MetPoint(
            email_point=point
        )


class MeetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "MeetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} you have forgotten what happen during the meeting",
            f"tell {pronoun} you would like to meet again",
            f"tell {pronoun} you did not attend the previous meeting",
            f"tell {pronoun} now is not a good time for you to have meeting",
            f"tell {pronoun} the meeting is cancelled",
            f"tell {pronoun} you want to postpone the meeting",
            f"say the meeting with {pronoun} is going to happen soon",
            f"say you remember the previous meeting with {pronoun}",
            f"say you need another time for the meeting with {pronoun}",
            f"say you might not attend the meeting with {pronoun}",
            f"say the meeting with {pronoun} might include other people",
            f"say you want to add other topics for the meeting",
            f"thank {pronoun} for rescheduling the meeting",
            f"thank {pronoun} for having the meeting with you",
            f"thank {pronoun} for able to be there for the meeting",
            f"scold {pronoun} for scheduling too many meetings",
            f"scold {pronoun} for meeting with another person instead of you",
            f"scold {pronoun} for not attending the meeting"
        ])
        return MeetPoint(
            email_point=point
        )


class CallPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PositivePoint":
        pronoun = "him" if is_male else "her"
        time = random.choice(["morning", "afternoon", "evening"])
        point = random.choice([
            f"tell {pronoun} it was great call with {pronoun}",
            f"tell {pronoun} the call with {pronoun} is nice",
            f"tell {pronoun} the to be nice during the call",
            f"tell {pronoun} to stop calling you",
            f"tell {pronoun} to call you in the {time}",
            f"tell {pronoun} that {time} is not a good time to call you",
            f"say you miss the call from {pronoun} this {time}",
            f"say you cannot receive call from {pronoun} in the {time}",
            f"say you want call {pronoun}",
            f"say the call from {pronoun} will always be ignored",
            f"say you had a hard time on call with {pronoun}",
            f"say you need another call with {pronoun}",
            f"thank {pronoun} for the call this {time}",
            f"thank {pronoun} for not calling in the {time}",
            f"thank {pronoun} for alerting you through a call",
            f"scold {pronoun} for calling you repeatedly",
            f"scold {pronoun} for not calling you",
            f"scold {pronoun} for calling the wrong phone number"
        ])
        return CallPoint(
            email_point=point
        )


class PlanPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PlanPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} it was a great plan",
            f"tell {pronoun} there is a need for planning",
            f"tell {pronoun} you have a new plan",
            f"tell {pronoun} the plan need to be changed",
            f"tell {pronoun} to choose between the different plans",
            f"tell {pronoun} the plan is going to fail",
            f"say you are more familiar with the restructuring planned for next Quarter",
            f"say you have plans for the current issues",
            f"say you need to meet with {pronoun} to discuss about the plan",
            f"say you planned to have different idea from {pronoun}",
            f"say the plan from {pronoun} is not feasible",
            f"say you are undergoing the plan already",
            f"thank {pronoun} for understanding your plan",
            f"thank {pronoun} for following the plan",
            f"thank {pronoun} for not forsaking the plan",
            f"scold {pronoun} for having a different plan in mind",
            f"scold {pronoun} for not planning properly",
            f"scold {pronoun} for giving the plan away to other people"
        ])
        return PlanPoint(
            email_point=point
        )


class MailPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "MailPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} the email from you is important",
            f"tell {pronoun} there is no need for email",
            f"tell {pronoun} you prefer email than meeting",
            f"tell {pronoun} email the correct person",
            f"tell {pronoun} to converse with you through email",
            f"tell {pronoun} to read the email from you",
            f"say you are contactable through email",
            f"say you need {pronoun} to forward the email to other people",
            f"say you want {pronoun} to be contactable through email",
            f"say you emailed {pronoun} important documents",
            f"say you have too many email to scan through",
            f"say you miss the email from {pronoun},
            f"thank {pronoun} for reading your email",
            f"thank {pronoun} for emailing you the documents",
            f"thank {pronoun} for the quick respone to your email",
            f"scold {pronoun} for missing too many emails",
            f"scold {pronoun} for emailing with an incorrect tone",
            f"scold {pronoun} for having to be reminded everytime to read email"
        ])
        return MailPoint(
            email_point=point
        )


class SchoolPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "SchoolPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} you do not know the content",
            f"tell {pronoun} you need help in studying",
            f"tell {pronoun} you can help {pronoun} to study",
            f"tell {pronoun} to study the correct content",
            f"tell {pronoun} to follow the study plan",
            f"tell {pronoun} now is a good time for a study session",
            f"say you are good with the content",
            f"say you need more time to finish the assignment",
            f"say you want to learn more from {pronoun}",
            f"say you are busy with school currently",
            f"say you do not know how to study",
            f"say the help in your study from {pronoun} is great",
            f"thank {pronoun} for provinding a great learning experience",
            f"thank {pronoun} for helping you in understanding the context",
            f"thank {pronoun} for studying with you",
            f"scold {pronoun} for ignoring you while you had help {pronoun} before",
            f"scold {pronoun} for not studying and receive bad grade",
            f"scold {pronoun} for dropping out of school"
        ])
        return SchoolPoint(
            email_point=point
        )