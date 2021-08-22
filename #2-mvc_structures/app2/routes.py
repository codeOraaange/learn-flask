from app2 import api, web
from app2.controllers import MyController, MyViewController

api.add_resource(MyController.MyController, '/')

web.add_resource(MyViewController.MyView, '/')

web.add_resource(MyViewController.MySecondView, '/say-my-name')
