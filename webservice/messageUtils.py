from webservice.response import Response, ResponseContext
from process.status import Status

class MessageUtils:

    @staticmethod
    def successResponse(context, data):
        return Response(ResponseContext(context, Status.SUCCESS), data).toString()

    @staticmethod
    def failureResponse(context, data):
        return Response(ResponseContext(context, Status.FAILURE), data).toString()
