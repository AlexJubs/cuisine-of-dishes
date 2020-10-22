# this was written by Alexander Jabbour on Oct 21
from flask import Flask
from flask import request
from aws_utils import aws_utils

app = Flask(__name__)

@app.route('/')
def initialize():
	return aws_utils.assert_table_exists()

@app.route('/add_dish')
def add_dish():
	dish = request.args["dish_name"]
	print(f"Adding dish with name {dish}")
	return aws_utils.add_dish(dish)

@app.route('/remove_dish')
def remove_dish():
	dish = request.args["dish_name"]
	print(f"Removing dish with name {dish}")
	return aws_utils.remove_dish(dish)

@app.route('/get_all_dishes')
def get_all_dishes():
	return aws_utils.get_all_dishes()

@app.route('/clear_all_dishes')
def clear_all_dishes():
	return aws_utils.clear_table()