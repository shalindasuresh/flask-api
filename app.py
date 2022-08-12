import os
import json

from dotenv import dotenv_values
from flask import Flask
from pymongo import MongoClient

config = dotenv_values(".env")
client = MongoClient(f'mongodb+srv://{config["MONGO_USER"]}:{config["MONGO_PASS"]}@{config["CLUSTER_ENDPOINT"]}/?retryWrites=true&w=majority')
db = client[config["MONGO_DB"]]
customers = db['customers']

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return "<h1>Welcome to FLASK Rest API</h1>"

@app.route("/customers/{customer_id}", methods=['GET'])
def get_customer():
    return "<h1>Get Customer List</h1>"

@app.route("/customers/list", methods=['GET'])
def get_customers():
    
    customer_list=[]
    for customer in customers.find():
        customer_list.append(customer)
    
    return json.dumps(customer_list, default=str)

@app.route("/customers", methods=['POST'])
def add_customer():
    customer={"first_name": "John", "last_name": "Doe"}
    customer_id = customers.insert_one(customer).inserted_id
    
    return customer_id

@app.route("/customers", methods=['PUT'])
def update_customer():
    return "<h1>Update Customer</h1>"

@app.route("/customers", methods=['DELETE'])
def remove_customer():
    return "<h1>Delete Customer</h1>"
