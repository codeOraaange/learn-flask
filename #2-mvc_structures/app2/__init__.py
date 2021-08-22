from flask import Flask # Memanggil library Flask
from flask_restful import Api # Memanggil library RESTful

app2 = Flask(__name__, template_folder='views')
api = Api(app2, prefix='/api') # Melakukan inisialisasi terhadap library RESTful untuk route api
web = Api(app2) # Melakukan inisialisasi terhadap library RESTful untuk route web

from app2 import routes # Memanggil file routes 
