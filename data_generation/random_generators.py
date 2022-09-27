import random


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
