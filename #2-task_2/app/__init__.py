from flask import Flask
from flask_restful import Api

app = Flask(__name__, template_folder='views')
api = Api(app, prefix='/mvc') 

from app import routes
