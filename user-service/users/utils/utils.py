# utils/id_generator.py

import uuid


def generate_user_id(role: str) -> str:
    role_prefix = {
        "admin": "1",
        "organizer": "2",
        "attendee": "3",
        "guest": "4",
    }
    prefix = role_prefix.get(role, "0")
    unique_suffix = str(uuid.uuid4().int)[:7]
    unique_id = f"{prefix}{unique_suffix}"
    return unique_id


def generate_unique_user_id(model, role):
    while True:
        role_prefix = {
            "admin": "1",
            "organizer": "2",
            "attendee": "3",
            "guest": "4",
        }
        prefix = role_prefix.get(role, "0")
        unique_suffix = str(uuid.uuid4().int)[:7]
        unique_id = f"{prefix}{unique_suffix}"
        if not model.objects.filter(id=unique_id).exists():
            return unique_id
