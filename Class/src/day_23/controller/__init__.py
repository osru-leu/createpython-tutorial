""" Controller __init__.py """
from flask_restx import Api

# Import namespaces from the controllers here below.
# Example: from .<file_name> import <namespace> as <namespace_ns>

from .players import NS as players_ns

API = Api(
    version='0.1.0',
    title='Python Sample Restx API',
    description='REST API for generic api functionality'
    )

# Add the namespaces to the API below here
# Example: API.add_namespace(<namespace>)
API.add_namespace(players_ns)