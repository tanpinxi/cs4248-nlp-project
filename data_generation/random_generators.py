import random

def get_random_day():
    day = random.choice([
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ])
    return f"{day}"

def get_random_time():
    digit = random.randint(1, 12)
    am_pm = random.choice(["am", "pm"])
    return f"{digit} {am_pm}"

def get_random_room():
    room = random.choice([
        "meeting room",
        "conference room",
        "seminar room",
    ])
    digit = random.randint(1, 10)
    return f"{room} {digit}"

def get_random_meeting_platform():
    platform = random.choice([
        "Zoom",
        "Google Meet",
        "Skype",
        "Microsoft Teams",
        "Slack",
    ])
    return f"{platform}"

def get_random_document():
    document = random.choice([
        "legal contract",
        "contract",
        "financial report",
        "business report",
        "report",
        "file",
        "Word document",
        "Excel spreadsheet"
        "PDF document",
        "schedule",
        "invoice",
        "quotation",
        "proposal",
        "diagram",
        "draft",
    ])
    return f"{document}"

def get_random_office_role():
    role = random.choice([
        "secretary",
        "HR manager",
        "team leader",
        "supervisor",
        "department head",
        "group director",
        "chairman",
        "director",
        "deputy CEO",
        "CEO",
        "client"
    ])
    return f"{role}"