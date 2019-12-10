import logging

from flask_restplus import Api

import config
from store.store import Store

log = logging.getLogger(__name__)
api = Api(version=config.API_VERSION, title=config.API_TITLE,description=config.API_DESC)
store = Store()


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not config.FLASK_DEBUG:
        return {'message': message}, 500


class SchemaUtils(object):
    
    @staticmethod
    def get_id(data):
        return data.get('id');

    @staticmethod
    def get_type(data):
        return data.get('type');

    @staticmethod
    def get_data(data, request_type):
        return data.get('data').get(request_type);