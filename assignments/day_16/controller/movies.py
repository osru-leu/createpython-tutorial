""" Movies Endpoint """
from flask import request
from flask_restx import Namespace, Resource, fields

from service.movies import Movies

NS = Namespace(
    'movies',
    description='Operations related to movies'
)

MOVIE = NS.model(
    'Movie', {
        'title': fields.String(
            required=True,
            description='Movie title',
            example='Django Unchained'
        ),
        'genre': fields.String(
            required=True,
            description='Movie type',
            example='Drama/Action'
        )
    }
)


@NS.route("")
class MoviesCollection(Resource):
    """ Movies Collection methods """

    def get(self):
        """ Returns list of movies """
        return Movies().get_all()
    @NS.expect(MOVIE)
    def post(self):
        """ Creates a movie """
        return Movies().create_one(request.get_json())


@NS.route("/<string:name>")
class Movie(Resource):
    """ Movie methods """

    def get(self, name):
        """ Returns a movie name """
        return Movies().get_one(name)

    def put(self, name):
        """ Updates a movie name """
        return Movies().update_one(name, request.json)

    def delete(self, name):
        """ Deletes a movie by name """
        return Movies().delete_one(name)
