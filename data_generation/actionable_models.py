import random

from data_generation.random_generators import get_random_room, get_random_time, get_random_day, \
    get_random_meeting_platform, get_random_document, get_random_office_role, get_random_first_name, \
    get_random_meeting_topic 
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
        summarized_point = f"book a meeting at {time} for {day}"
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
        summarized_point = f"schedule an online meeting on at {time} for {day}"
        return BookOnlineMeetingPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )

class PostponeMeetingPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "PostponeMeetingPoint":
        action = random.choice(["postpone", "reschedule", "delay", "rearrange", "call off"])
        platform = random.choice([f" {get_random_meeting_platform()}", ""])
        day = random.choice([f"next {get_random_day()}",  f"this {get_random_day()}", "tomorrow"])
        email_point = random.choice([
            f"{action} the{platform} meeting scheduled for {day}",
        ])
        summarized_point = f"postpone the meeting scheduled for {day}"
        return PostponeMeetingPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )

class ConfirmMeetingAgendaPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "ConfirmMeetingAgendaPoint":
        action = random.choice(["confirm", "check", "verify"])
        day = random.choice([f"next {get_random_day()}",  f"this {get_random_day()}", "tomorrow", "today"])
        topic = get_random_meeting_topic()
        email_point = random.choice([
            f"{action} that {day}'s meeting agenda is about {topic}",
        ])
        summarized_point = f"confirm that {day}'s meeting agenda is about {topic} "
        return ConfirmMeetingAgendaPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )

# Attachments 
class ReviewAttachmentPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "ReviewAttachmentPoint":
        pronoun = "his" if is_male else "her"
        action = random.choice(["review", "critique", "evaluate", "scrutinize", "examine", "take a look at"])
        document = get_random_document()
        day = random.choice([f"next {get_random_day()}",  f"this {get_random_day()}", "tomorrow"])
        email_point = random.choice([
            f"{action} the attached {document} by {day}",
            f"{action} the enclosed {document} by {day}",
            f"find the attached {document} for {pronoun} review by {day}",
        ])
        summarized_point = f"review the attached document by {day}"
        return ReviewAttachmentPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )

class CompleteAttachmentPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "CompleteAttachmentPoint":
        action = random.choice(["fill in", "fill up", "complete", "finalize", "submit"])
        day = random.choice([f"next {get_random_day()}",  f"this {get_random_day()}", "tomorrow", "today"])
        time = get_random_time()
        email_point = random.choice([
            f"{action} the attached form by {day} {time}",
            f"{action} and reply with the enclosed form by {day} {time}",
        ])
        summarized_point = f"fill in the attached form by {day} {time}"
        return CompleteAttachmentPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )

class ForwardAttachmentPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "ForwardAttachmentPoint":
        pronoun = "his" if is_male else "her"
        role = get_random_office_role()
        recipient = random.choice([f"{pronoun} {role}", get_random_first_name()])
        action = random.choice(["forward", "email", "send"])
        document = get_random_document()
        email_point = random.choice([
            f"{action} the {document} to {recipient}",
        ])
        summarized_point = f"forward the document to {recipient}"
        return ForwardAttachmentPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )
        
# Requests
class RequestExtensionPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "RequestExtensionPoint":
        action = random.choice(["extend", "postpone", "prolong"])
        reason = random.choice(["recent physical injury", "recent mental ill-health", "personal reasons", "family emergency", "sick leave"])
        document = get_random_document()
        email_point = random.choice([
            f"{action} deadline for submission of {document} due to {reason}",
        ])
        summarized_point = f"extend deadline for submission of {document} due to {reason}"
        return RequestExtensionPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )

class ApproveRequestPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "ApproveRequestPoint":
        name = get_random_first_name()
        action = random.choice(["approve", "allow", "accept", "endorse", "ratify", "validate"])
        request = random.choice(["have work from home arrangement", 
                                 "have hybrid work arrangement", 
                                 "take medical leave", 
                                 "extend deadline", 
                                 "get more manpower", 
                                 "get more resources"])
        email_point = random.choice([
            f"{action} {name}'s request to {request}",
        ])
        summarized_point = f"approve {name}'s request to {request}"
        return ApproveRequestPoint(
            email_point=email_point,
            summarized_point=summarized_point,
        )