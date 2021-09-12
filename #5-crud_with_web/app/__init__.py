
from flask import Flask
from flask_restful import Api
from app.config import Config

app = Flask(
    __name__, 
    template_folder='views',
    static_url_path='/public', 
    static_folder='../public',
)
app.config.from_object(Config)

api = Api(app, prefix='/api')
web = Api(app)

from flask_jwt_extended import JWTManager
jwt = JWTManager(app)

from app.db_manager import DatabaseManager
DatabaseManager.open_database()

from app import routes
