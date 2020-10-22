# this was written by Alexander Jabbour on Oct 21
import boto3

# dynamodb util for storing dishes
TableName = "Dishes"
dynamodb_client = boto3.client("dynamodb")

class aws_utils:
    def assert_table_exists():
        # if table exists, return, otherwise craete table
        if TableName in dynamodb_client.list_tables()["TableNames"]:
            return "Dishes table already exists!"

        # create table in dynamo
        response = dynamodb_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Dish',
                'AttributeType': 'S',
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'Dish',
                'KeyType': 'HASH',
            }
        ],
        TableName=TableName,
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
        )
        # if we run into an effor creating the table
        if ("TableDescription" not in response):
            return "Error creating dynamo table \n {}".format(response)

        # otherwise, all is good
        return "Created table in DynamoDB for your dishes!"

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
