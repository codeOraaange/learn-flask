from flask_restful import Resource
from flask import render_template, make_response, request

class MyView(Resource):
    def get(self):
        view = render_template('index.html')
        return make_response(view)


class MySecondView(Resource):
    def get(self):
        name = request.args.get('name') # Mengambil argumen nama pada URL
        age = request.args.get('age') 

        if not name: # Pengecekan kondisi apabila name kosong, maka digantikan dengan default name yaitu Orange
            name = "Orange"
        if not age:
            age = 0

        view = render_template('say-my-name.html', name_render=name, age_render=age)
        return make_response(view)
