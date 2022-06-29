from dataclasses import dataclass
from model.user import User


@dataclass
class Message:
    from_user: User
    to_user: User
    message: str
