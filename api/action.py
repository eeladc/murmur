from api.api import store, SchemaUtils
import logging.config

log = logging.getLogger(__name__)


class BasicAction(object):

    @staticmethod
    def push(request):
        request_type = SchemaUtils.get_type(request)
        print(request_type)
        savable_data = SchemaUtils.get_data(request, request_type)
        if not store.index_exists(request_type):
            store.create_index(request_type)
        store.insert(request_type, SchemaUtils.get_id(savable_data), savable_data)
        return True

    @staticmethod
    def search(request):
        return store.multi_search(SchemaUtils.get_type(request), request.get('text'), 1, 10, request.get('fields'))
