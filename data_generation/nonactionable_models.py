import random

from data_generation.util_models import NonActionablePoint
from data_generation.random_generators import get_random_task, get_random_office_role, get_random_daytime


class PositiveMetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PositiveMetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} it was great meeting {pronoun}",
            f"tell {pronoun} you had a good catchup with {pronoun}",
            f"tell {pronoun} you appreciate to have met {pronoun}",
            f"tell {pronoun} getting to see {pronoun} was a good experience",
            f"tell {pronoun} you now know {pronoun} better",
            f"say you had a nice chat with {pronoun}",
            f"say the conversation with {pronoun} is great",
            f"say you want to keep in touch with {pronoun}",
            f"thank {pronoun} for providing time for you",
            f"thank {pronoun} for not ignoring you",
            f"thank {pronoun} for helping you during the catchup"
        ])
        return PositiveMetPoint(
            email_point=point
        )

class NegativeMetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "NegativeMetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} you regret meeting {pronoun}",
            f"say the talk with {pronoun} is bad",
            f"say you do not want to meet {pronoun} again",
            f"scold {pronoun} for being unresponsive",
            f"scold {pronoun} for giving you a hard time",
            f"scold {pronoun} for wasting your time"
        ])
        return NegativeMetPoint(
            email_point=point
        )

class PositiveMeetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PositiveMeetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"say the meeting with {pronoun} was constructive",
            f"say the meeting with {pronoun} was pleasant",
            f"say you enjoyed the previous meeting with {pronoun}",
            f"say that other people will be joining the meeting with {pronoun} later",
            f"thank {pronoun} for rescheduling the meeting",
            f"thank {pronoun} for having the meeting with you",
            f"thank {pronoun} for able to be there for the meeting"
        ])
        return PositiveMeetPoint(
            email_point=point
        )

class NegativeMeetPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "NegativeMeetPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} you did not attend the previous meeting",
            f"tell {pronoun} the meeting is cancelled",
            f"say you might not attend the meeting with {pronoun}",
            f"say the meeting with {pronoun} was not constructive",
            f"say the meeting with {pronoun} was not useful",
            f"say the meeting with {pronoun} was unpleasant",
            f"scold {pronoun} for not attending the meeting",
            f"scold {pronoun} for missing the meeting",
        ])
        return NegativeMeetPoint(
            email_point=point
        )

class PositiveCallPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PositiveCallPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} it was great call with {pronoun}",
            f"tell {pronoun} the call with {pronoun} was nice",
            f"tell {pronoun} the call with {pronoun} was enjoyable",
            f"tell {pronoun} that the call was pleasant",
            f"thank {pronoun} for the call this {get_random_daytime()}",
            f"thank {pronoun} for not calling in the {get_random_daytime()}",
            f"thank {pronoun} for alerting you through a call",
        ])
        return PositiveCallPoint(
            email_point=point
        )

class NegativeCallPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "NegativeCallPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} to stop calling you for no reason",
            f"tell {pronoun} that the call was unpleasant",
            f"tell {pronoun} that the call was not enjoyable",
            f"tell {pronoun} that {get_random_daytime()} is not a good time to call you",
            f"say the call from {pronoun} will always be ignored from now on",
            f"say you had a hard time on call with {pronoun}",
            f"scold {pronoun} for calling you repeatedly",
        ])
        return NegativeCallPoint(
            email_point=point
        )

class PositivePlanPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PositivePlanPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} it was a great plan",
            f"tell {pronoun} there is a need for planning",
            f"tell {pronoun} you have a new plan",
            f"tell {pronoun} the plan need to be changed",
            f"tell {pronoun} to choose between the different plans",
            f"say you have plans for the current issues",
            f"say you need to meet with {pronoun} to discuss about the plan",
            f"say you planned to have different idea from {pronoun}",
            f"say you are undergoing the plan already",
            f"thank {pronoun} for understanding your plan",
            f"thank {pronoun} for following the plan",
            f"thank {pronoun} for not forsaking the plan"
        ])
        return PositivePlanPoint(
            email_point=point
        )

class NegativePlanPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "NegativePlanPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} the plan is going to fail",
            f"say the plan from {pronoun} is not feasible",
            f"say the plan from {pronoun} cannot be done due to time",
            f"say the plan from {pronoun} cannot be done due to budget",
            f"scold {pronoun} for having a different plan in mind",
            f"scold {pronoun} for giving the plan away to other people"
        ])
        return NegativePlanPoint(
            email_point=point
        )

class SoloIntroPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "SoloIntroPoint":
        pronoun = "him" if is_male else "her"
        pronoun_2 = "his" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} that you are a new hire and have recently joined {pronoun_2} team",
            f"tell {pronoun} that you are looking forward to learning from {pronoun} and the rest of the team",
            f"tell {pronoun} that you are looking forward to getting to know the team members"
            f"tell {pronoun} that you are hoping for a pleasant work experience with everyone"
        ])
        return SoloIntroPoint(
            email_point=point
        )

class PositiveReviewPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PositiveReviewPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} you admire the quality of their work in the recent {get_random_task()}",
            f"tell {pronoun} to keep up the good work",
            f"say that you look forward to working with {pronoun} in the future"
        ])
        return PositiveReviewPoint(
            email_point=point
        )

class NegativeReviewPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "NegativeReviewPoint":
        pronoun = "him" if is_male else "her"
        pronoun_2 = "his" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} that the recent {get_random_task()} done by {pronoun} was disappointing",
            f"tell {pronoun} that {pronoun_2} performance reflects poorly on {pronoun_2} work standards",
            f"say that you expect better result from {pronoun} in the future"
        ])
        return NegativeReviewPoint(
            email_point=point
        )

class PositiveMailPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PositiveMailPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} the email from you is important",
            f"tell {pronoun} there is no need for email",
            f"tell {pronoun} you prefer email than meeting",
            f"tell {pronoun} email the correct person",
            f"tell {pronoun} to converse with you through email",
            f"tell {pronoun} to read the email from you",
            f"say you are contactable through email",
            f"say you emailed {pronoun} important documents",
            f"thank {pronoun} for reading your email",
            f"thank {pronoun} for emailing you the documents",
            f"thank {pronoun} for the quick response to your email",
        ])
        return PositiveMailPoint(
            email_point=point
        )

class NegativeMailPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "NegativeMailPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"say you have too many email to scan through",
            f"say you miss the email from {pronoun}",
            f"scold {pronoun} for missing too many emails",
            f"scold {pronoun} for emailing with an incorrect tone",
            f"scold {pronoun} for having to be reminded everytime to read email"
        ])
        return NegativeMailPoint(
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
            f"say you are busy with school currently",
            f"say you do not know how to study",
            f"say the help in your study from {pronoun} is great",
            f"thank {pronoun} for providing a great learning experience",
            f"thank {pronoun} for helping you in understanding the context",
            f"thank {pronoun} for studying with you",
            f"scold {pronoun} for ignoring you while you had helped {pronoun} before",
            f"scold {pronoun} for not studying and receive bad grade",
            f"scold {pronoun} for dropping out of school"
        ])
        return SchoolPoint(
            email_point=point
        )

class ThankPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "ThankPoint":
        pronoun = "him" if is_male else "her"
        pronoun_2 = "his" if is_male else "her"
        pronoun_3 = "he" if is_male else "she"
        point = random.choice([
            f"thank {pronoun} for the help that {pronoun_3} provided in the recent {get_random_task()}",
            f"tell {pronoun} that {pronoun_2} assistance is greatly appreciated",
            f"tell {pronoun} to not hesitate to let you know if they need assistance in the future",
            f"tell {pronoun} that you are grateful for the help",
            f"thank {pronoun} for giving you the time of day",
            f"thank {pronoun} for such a wonderful contribution to the recent {get_random_task()}",
            f"thank {pronoun} putting a good word to the {get_random_office_role()}",
            f"show your gratitude to {pronoun} by offering your assistance to his current job",
            f"thank {pronoun} for {pronoun_2} service",
            f"thank {pronoun} for {pronoun_2} application to the role",
            f"thank {pronoun} for reading the email and for {pronoun} to have a great day ahead"
        ])
        return ThankPoint(
            email_point=point
        )

class ApologyPoint(NonActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "ApologyPoint":
        pronoun = "him" if is_male else "her"
        point = random.choice([
            f"tell {pronoun} that you would like to apologise for the trouble caused",
            f"tell {pronoun} that you are sorry for not performing your role up to par",
            f"tell {pronoun} that you will not repeat the mistake again",
            f"tell {pronoun} that you would like to apologize for the inconvenience caused",
            f"tell {pronoun} that you are sorry for the trouble caused",
            f"inform {pronoun} that you and your team are responsible for the issues caused, and would like to make things right",
            f"tell {pronoun} that you are sorry for the poor-quality work",
            f"tell {pronoun} that you are aware of the mistakes made, and would like to make amends"
        ])
        return ApologyPoint(
            email_point=point
        )
