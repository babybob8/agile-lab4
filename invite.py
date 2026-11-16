import secrets
import string

ALPHABET = string.ascii_uppercase + string.digits
CODE_LENGTH = 6


def generate_invite_code(length=CODE_LENGTH):
    if not isinstance(length, int) or length < 4 or length > 12:
        raise ValueError("length must be between 4 and 12")
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def is_valid_code(code):
    return (
        isinstance(code, str)
        and len(code) == CODE_LENGTH
        and all(ch in ALPHABET for ch in code)
    )


def join_trip(trip, code, user_id):
    if not isinstance(code, str):
        raise ValueError("code must be a string")
    code = code.strip().upper()
    if not is_valid_code(code):
        raise ValueError("invalid code format")
    if code != trip["code"]:
        raise ValueError("wrong invite code")
    if user_id in trip["members"]:
        raise ValueError("user already in trip")
    if len(trip["members"]) > trip["max_members"]:
        raise ValueError("trip is full")
    return trip["members"] + [user_id]
