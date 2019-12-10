from elasticsearch import Elasticsearch

import config
from store.query import multi_search


class Store(object):

    def __init__(self):
        super().__init__()
        self.es = Elasticsearch(config.ES_URL)

    def insert(self, index, id, data):
        return self.es.index(index=index, doc_type=config.DOC_TYPE, id=id, body=data)

    def search(self, index, query_text):
        return self.es.search(index=index, body={'query': {'match': {'text': query_text}}})

    def multi_search(self, index, keyword, page_no, page_size, *fields):
        return self.es.search(index=index, body=multi_search(keyword=keyword, page_no=page_no, page_size=page_size))

    def index_exists(self, index):
        return self.es.indices.exists(index=index)

    def create_index(self, index, cfg=config.DEFAULT_ES_INDEX_CONFIG):
        return self.es.indices.create(index=index, body=cfg)
