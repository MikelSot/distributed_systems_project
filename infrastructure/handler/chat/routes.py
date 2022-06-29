from . import my_blue_message
from model.message import Message

@my_blue_message.route("/api/v1/<from_>",  methods=["GET"])
def message_from():
    print("ds")


