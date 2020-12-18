''' Controller __init__.py '''
from flask_restx import Api

#Import namespace from controller
from .games import NS as games_ns
from .players import NS as players_ns

API = Api(
    version='0.1.0',
    title='Connect Four Restx API',
    description='REST API for generic api functionality'
)
#Add namespaces to the API
API.add_namespace(games_ns)
API.add_namespace(players_ns)