from flask_restful import Resource
from flask import render_template, make_response, request

class Conditional(Resource):
    def get(self):
        x = request.args.get('x')
        y = request.args.get('y') 

        if x and y:
            view = render_template('Fulfilled.html', x_render=x, y_render=y)
        else:
            view = render_template('NotFulfilled.html')

        return make_response(view)
