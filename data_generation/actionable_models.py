import random

from data_generation.random_generators import (
    get_random_room,
    get_random_time,
    get_random_day,
    get_random_meeting_platform,
    get_random_document,
    get_random_office_role,
    get_random_first_name,
    get_random_meeting_topic,
)
from data_generation.util_models import ActionablePoint


# Scheduling
class BookMeetingPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "BookMeetingPoint":
        action = random.choice(["schedule", "book", "plan", "arrange", "set up"])
        meeting = random.choice(["meeting", "chat", "discussion", "review", "sharing"])
        location = random.choice([f" in {get_random_room()}", ""])
        day = random.choice([f"next {get_random_day()}", f"this {get_random_day()}", "tomorrow"])
        time = get_random_time()
        email_point = random.choice([
            f"{action} a {meeting}{location} at {time} for {day}",
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
        meeting = random.choice(["meeting", "chat", "discussion", "review", "sharing"])
        platform = random.choice([f"{get_random_meeting_platform()}"])
        day = random.choice([f"next {get_random_day()}", f"this {get_random_day()}", "tomorrow"])
        time = get_random_time()
        email_point = random.choice([
            f"{action} a {meeting} on {platform} at {time} for {day}",
            f"send a {platform} invitation for {day} at {time}",
            f"create a {platform} {meeting} invite for {day} at {time}"
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
        meeting = random.choice(["meeting", "chat", "discussion", "review", "sharing"])
        day = random.choice([f"next {get_random_day()}", f"this {get_random_day()}", "tomorrow"])
        email_point = random.choice([
            f"{action} the{platform} {meeting} scheduled for {day}",
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
        meeting = random.choice(["meeting", "chat", "discussion", "review", "sharing"])
        day = random.choice([f"next {get_random_day()}", f"this {get_random_day()}", "tomorrow", "today"])
        topic = get_random_meeting_topic()
        email_point = random.choice([
            f"{action} that {day}'s {meeting} agenda is about {topic}",
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
        day = random.choice([f"next {get_random_day()}", f"this {get_random_day()}", "tomorrow"])
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
        document = get_random_document()
        day = random.choice([f"next {get_random_day()}", f"this {get_random_day()}", "tomorrow", "today"])
        time = get_random_time()
        email_point = random.choice([
            f"{action} the attached {document} by {day} {time}",
            f"{action} and reply with the enclosed {document} by {day} {time}",
        ])
        summarized_point = f"fill in the attached document by {day} {time}"
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
        action = random.choice(["extend", "postpone", "prolong", "delay"])
        deadline = random.choice(["deadline", "due date", "timeline"])
        reason = random.choice([
            "recent physical injury",
            "recent mental ill-health",
            "personal reasons",
            "family emergency",
            "sick leave",
            "unforeseen circumstances",
            "urgent matters",
            "new priorities",
            "power outages",
            "unexpected delays",
        ])
        document = get_random_document()
        email_point = random.choice([
            f"{action} {deadline} for submission of {document} due to {reason}",
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
        request = random.choice([
            "have work from home arrangement",
            "have hybrid work arrangement",
            "take medical leave",
            "go on medical leave",
            "extend deadline",
            "get more manpower",
            "get more resources",
            "take leave",
            "go on paid leave",
            "increase headcount",
            "go on childcare leave",
        ])
        email_point = random.choice([
            f"{action} {name}'s request to {request}",
        ])
        summarized_point = f"approve {name}'s request to {request}"
        return ApproveRequestPoint(
            email_point=email_point,
            summarized_point=summarized_point
        )


class RequestUpdatePoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "RequestUpdatePoint":
        update = random.choice(["status", "progress", "development"])
        adjective = random.choice(["", "most recent ", "latest ", "last known ", "current "])
        email_point = random.choice([
            f"give me an update on the {adjective}{update}",
            f"let me know what is the {adjective}{update}",
            "let me know how things are going",
            f"provide me with an update on the {adjective}{update}"
        ])
        summarized_point = f"give an update"
        return RequestUpdatePoint(
            email_point=email_point,
            summarized_point=summarized_point
        )


# Response
class RequestResponsePoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "RequestResponsePoint":
        passive = "him" if is_male else "her"
        pronoun = "he" if is_male else "her"
        action = random.choice(["reply to", "acknowledge"])
        day = random.choice([f"next {get_random_day()}", f"this {get_random_day()}", "tomorrow", "today"])
        email_point = random.choice([
            f"{action} this email by {day}",
            f"look forward to hear from {passive} by {day}",
            f"give us a reply by {day}",
            f"let us know that {pronoun} has received the email by {day}",
        ])
        summarized_point = f"acknowledge this email by {day}"
        return RequestResponsePoint(
            email_point=email_point,
            summarized_point=summarized_point
        )


class FeedbackPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "FeedbackPoint":
        possessive = "his" if is_male else "her"
        pronoun = "he" if is_male else "her"
        action = random.choice(["give", "tell"])
        feedback = random.choice(["feedback", "opinions", "suggestions", "recommendations", "thoughts", "ideas"])
        email_point = random.choice([
            f"{action} us {possessive} {feedback}",
            f"let us know {possessive} {feedback}",
            f"tell us what {pronoun} think",
            f"let us know what {pronoun} think",
            f"share with us what some {feedback}",
        ])
        summarized_point = "give feedback"
        return FeedbackPoint(
            email_point=email_point,
            summarized_point=summarized_point
        )


# Clarifications
class ClarificationPoint(ActionablePoint):
    @staticmethod
    def init_point(is_male: bool) -> "ClarificationPoint":
        pronoun = "he" if is_male else "her"
        action = random.choice(["explain", "clarify", "go through"])
        action_with_preposition = random.choice([
            "shed some light",
            "give further explanations",
            "give more details",
            "give more context"
        ])
        general_topic = random.choice(["topic", "subject", "concept", "idea", "plan"])
        specific_topic = get_random_meeting_topic()
        topic = random.choice([general_topic, specific_topic])
        email_point = random.choice([
            f"{action} the {topic} again",
            f"{action_with_preposition} on the {topic}",
            f"{action_with_preposition} about what {pronoun} means",
        ])
        summarized_point = "explain the topic"
        return ClarificationPoint(
            email_point=email_point,
            summarized_point=summarized_point
        )
