# Import the necessary modules
from flask import Flask, jsonify, request

# Create a Flask app instance
app = Flask(__name__)


# Define a route for the root URL '/'
@app.route("/")
def index():
    return "Hello World"


# Define a route for the URL '/api/v1/get-data' with HTTP method 'GET'
@app.route("/api/v1/get-data", methods=["GET"])
def get_data():
    return jsonify({"data": "Hello World"})


# Define a route for the URL '/api/v1/post-data' with HTTP method 'POST'
@app.route("/api/v1/post-data", methods=["POST"])
def post_data():
    return jsonify({"data": "Hello World"})


# Define a route for the URL '/api/v1/put-data' with HTTP method 'PUT'
@app.route("/api/v1/put-data", methods=["PUT"])
def put_data():
    print(request.data)
    return jsonify({"data": "Hello World"})


# Define a route for the URL '/api/v1/delete-data' with HTTP method 'DELETE'
@app.route("/api/v1/delete-data", methods=["DELETE"])
def delete_data():
    return jsonify({"data": "Hello World"})


# Run the Flask app if this file is being executed directly
if __name__ == "__main__":
    app.run(debug=True)
