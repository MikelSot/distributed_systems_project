from dataclasses import dataclass
from model.message import Message

@dataclass
class MessageData:
    message: Message

    def add_message(self, message: Message):
        self.message = message

