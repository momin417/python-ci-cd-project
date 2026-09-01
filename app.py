from flask import Flask, jsonify

from calculator import add, divide, multiply, subtract

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Python CI/CD Calculator API",
            "status": "running",
        }
    )


@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return jsonify({"result": add(a, b)})


@app.route("/subtract/<int:a>/<int:b>")
def subtract_numbers(a, b):
    return jsonify({"result": subtract(a, b)})


@app.route("/multiply/<int:a>/<int:b>")
def multiply_numbers(a, b):
    return jsonify({"result": multiply(a, b)})


@app.route("/divide/<int:a>/<int:b>")
def divide_numbers(a, b):
    try:
        result = divide(a, b)
        return jsonify({"result": result})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run()