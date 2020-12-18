from flask_restx import Api

from .contact import NS as contacts_ns

API = Api(
    version='0.1.0',
    title='Address Book',
    description='a digital address book'
)

API.add_namespace(contacts_ns)