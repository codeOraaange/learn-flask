
from flask import Flask
from flask_restful import Api
from app.config import Config
from app.db_manager import DatabaseManager


app = Flask(__name__, template_folder='views')
app.config.from_object(Config)

api = Api(app, prefix='/api')
web = Api(app)

DatabaseManager.open_database() # Melakukan inisialisasi terhadap library database

from app import routes
