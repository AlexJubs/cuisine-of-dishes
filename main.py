# this was written by Alexander Jabbour on Oct 21
from flask import Flask
from flask import request
from aws_utils import aws_utils
from collections import Counter

app = Flask(__name__)

@app.route('/')
def initialize():
	return aws_utils.assert_table_exists()

@app.route('/add_dish')
def add_dish():
	dish = request.args["dish_name"]
	recipies = request.args.get("recipies")
	print(f"Adding dish with name {dish}")
	return aws_utils.add_dish(dish, recipies)

@app.route('/remove_dish')
def remove_dish():
	dish = request.args["dish_name"]
	print(f"Removing dish with name {dish}")
	return aws_utils.remove_dish(dish)

@app.route('/get_all_dishes')
def get_all_dishes():
	return str(aws_utils.get_all_dishes())

@app.route('/clear_all_dishes')
def clear_all_dishes():
	return aws_utils.clear_table()

@app.route('/get_dishes_by_recipies')
def get_dishes_by_recipies():
	ret = str()
	recipies = request.args["recipies"]
	recipies = Counter(recipies.split(", "))

	for dish in aws_utils.get_all_dishes():
		dish_recipies = Counter(dish["recipies"]["S"].split(", "))
		
		can_add = True

		for key in dish_recipies.keys():
			if key not in recipies:
				can_add = False
				break
			if recipies[key] < dish_recipies[key]:
				can_add = False
				break

		if (can_add):
			ret += dish["Dish"]["S"] + "\n"

	return ret