# this was written by Alexander Jabbour on Oct 21
import boto3

# dynamodb util for storing dishes

class aws_utils:
	def assert_table_exists():
		# if table exists, return, otherwise 
		return "ok"

	def get_all_dishes():
		return "ok"

	def add_dish(dish_name):
		# check if dish exists if no, return "dish already exists". if yes, return "removed <dish>"
		return "ok"

	def remove_dish(dish_name):
		# check is dish exists. if no, return error. if yes, return "removed <dish>"
		return "ok"

	def dish_exists(dish_name):
		return "ok"

	def clear_table():
		return "ok"
