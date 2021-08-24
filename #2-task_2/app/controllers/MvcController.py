from flask_restful import Resource
from flask import render_template, make_response, request

class Count(Resource):
    def get(self):
        method = request.args.get('method')
        first = request.args.get('first')
        second = request.args.get('second')

        if method and first and second:
            first = float(first)
            second = float(second)
            if method == "sum":
                method = "penjumlahan"
                result = first + second
            elif method == "divide":
                method = "pembagian"
                result = first / second
            elif method == "sub":
                method = "pengurangan"
                result = first - second
            elif method == "multiply":
                method = "perkalian"
                result = first * second
            elif method == "mod":
                method = "modulus"
                result = first % second
            elif method == "rank":
                method = "pangkat"
                result = first ** second

            view = render_template('Fulfilled.html', method_render=method, result_render=result)
        else:
            view = render_template('NotFulfilled.html')

        return make_response(view)
    