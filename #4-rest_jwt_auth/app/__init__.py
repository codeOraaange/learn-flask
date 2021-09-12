
from flask import Flask
from flask_restful import Api
from app.config import Config

app = Flask(__name__, template_folder='views')
app.config.from_object(Config)

api = Api(app, prefix='/api')
web = Api(app)

from app.db_manager import DatabaseManager
DatabaseManager.open_database()

from flask_jwt_extended import JWTManager
jwt = JWTManager(app)

from app import routes
