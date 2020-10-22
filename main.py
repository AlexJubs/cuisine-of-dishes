# this was written by Alexander Jabbour on Oct 21
from flask import Flask
from flask import request
from aws_utils import aws_utils

app = Flask(__name__)

@app.route('/')
def initialize():
	aws_utils.assert_table_exists()
	return "initialized table in DynamoDB for your dishes!"

@app.route('/add_dish')
def add_dish():
	dish = request.args["dish_name"]
	print(f"Adding dish with name {dish}")
	return aws_utils.add_dish(dish)

@app.route('/remove_dish')
def remove_dish():
	dish = request.args["dish_name"]
	print("Removing dish with name {}".format(dish))
	return aws_utils.remove_dish(dish)

@app.route('/get_all_dishes')
def get_all_dishes():
	dishes = aws_utils.get_all_dishes()
	return "ok"