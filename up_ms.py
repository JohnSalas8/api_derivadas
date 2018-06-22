from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api

from Services.Differentiation import Differentiation
from Services.DifferentiationToLeft import DifferentiationToLeft
from Services.DifferentiationToRight import DifferentiationToRight

app = Flask(__name__)
api = Api(app)

# http://localhost:1908/dhc/e^(-2*x+1)*cos(7*x-8)*(6*x^2-1)/1/0.01
@app.route('/dhc/<exp>/<x>/<h>')
def dhc(exp, x, h):
    return jsonify(
        Differentiation().differentation_centralized (
            unicode(exp), float(x), float(h)
        )
    )

# http://localhost:1908/dhd/e^(-2*x+1)*cos(7*x-8)*(6*x^2-1)/1/0.01
@app.route('/dhd/<exp>/<x>/<h>')
def dhd(exp, x, h):
    return jsonify(
        DifferentiationToRight().differentation_to_right (
            unicode(exp), float(x), float(h)
        )
    )

# http://localhost:1908/dhi/e^(-2*x+1)*cos(7*x-8)*(6*x^2-1)/1/0.01
@app.route('/dhi/<exp>/<x>/<h>')
def dhi(exp, x, h):
    return jsonify(
        DifferentiationToLeft().differentation_to_left (
            unicode(exp), float(x), float(h)
        )
    )

@app.route('/')
def index():
    return render_template('information.html')


if __name__ == '__main__':
    app.run(port=1908)
    