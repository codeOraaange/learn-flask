from app import api
from app.controllers import MvcController

api.add_resource(MvcController.Conditional, '/xy-parameter')
