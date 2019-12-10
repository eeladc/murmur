from flask import jsonify
import jsonpickle

class Message(object):

    def __init__(self, context, data):
        self.context = context
        self.data = data

    def toString(self):
        return jsonpickle.encode(self)
