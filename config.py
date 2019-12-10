# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False


API_VERSION='1.0'
API_TITLE='Murmur API'
API_DESC='APIs for tracking actions'

ES_URL=['localhost:9200']
DOC_TYPE='track'

DEFAULT_ES_INDEX_CONFIG = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}