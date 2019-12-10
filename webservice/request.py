import json
from webservice.message import Message

class Request(Message):
    def __init__(self, context, data):
        Message.__init__(self,context,data)
