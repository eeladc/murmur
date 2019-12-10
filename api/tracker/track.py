import logging

from flask import request, jsonify, make_response
from flask_restplus import Resource

from api.action import BasicAction
from api.api import api
from schema.model import track_data, search_track, trackType

log = logging.getLogger(__name__)

ns = api.namespace('tracker', description='Operations to tracker')


@ns.route('/')
class TrackData(Resource):

    @api.expect(track_data)
    def post(self):
        """
        Push a new tracker data
        """
        return BasicAction.push(request.json), 200


@ns.route('/search')
class TrackDataGet(Resource):

    @api.expect(search_track)
    def post(self):
        """
        Search tracker data
        """
        search_response = BasicAction.search(request.json)
        return make_response(jsonify(search_response['hits']), 200)
