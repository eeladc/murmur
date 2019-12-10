from enum import Enum

class Status(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    def describe(self):
        return self.value
