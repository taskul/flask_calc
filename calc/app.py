# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a', '0'))
    b = int(request.args.get('b', '0'))
    result = operations.add(a,b)
    return f'{result}'

@app.route('/sub')
def subtract():
    a = int(request.args.get('a', '0'))
    b = int(request.args.get('b', '0'))
    result = operations.sub(a,b)
    return f'{result}'

@app.route('/mult')
def multiply():
    a = int(request.args.get('a', '0'))
    b = int(request.args.get('b', '0'))
    result = operations.mult(a,b)
    return f'{result}'
    
@app.route('/div')
def divide():
    a = int(request.args.get('a', '0'))
    b = int(request.args.get('b', '0'))
    result = operations.div(a,b)
    return f'{result}'

@app.route('/math/<operator>')
def calculator(operator):
    math_operators = {
        'add': operations.add,
        'sub': operations.sub,
        'mult': operations.mult,
        'div': operations.div
    }
    a = int(request.args.get('a', '0'))
    b = int(request.args.get('b', '0'))
    result = math_operators[operator](a,b)
    return f'{result}'



if __name__ == '__main__':
    app.run()
