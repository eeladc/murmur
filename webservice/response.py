import json
from webservice.message import Message

class ResponseContext(object):

    def __init__(self,context,status):
        self.context = context
        self.status = status

class Response(Message):
    def __init__(self, context, data):
        Message.__init__(self,context,data)
