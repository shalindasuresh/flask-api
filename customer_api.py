from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return "<h1>Welcome to FLASK Rest API</h1>"

@app.route("/customers", methods=['GET'])
def get_customers():
    return "<h1>Get Customer List</h1>"

@app.route("/customers", methods=['POST'])
def add_customer():
    return "<h1>Add Customer</h1>"

@app.route("/customers", methods=['PUT'])
def update_customer():
    return "<h1>Update Customer</h1>"

@app.route("/customers", methods=['DELETE'])
def remove_customer():
    return "<h1>Delete Customer</h1>"
