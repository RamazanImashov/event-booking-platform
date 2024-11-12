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
    return f"{prefix}{unique_suffix}"
