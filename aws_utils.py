# this was written by Alexander Jabbour on Oct 21
import boto3

# dynamodb util for storing dishes
TableName = "Dishes"
dynamo = boto3.client("dynamodb")

class aws_utils:
    def assert_table_exists():
        # if table exists, return, otherwise craete table
        if TableName in dynamo.list_tables()["TableNames"]:
            return "Dishes table already exists!"

        # create table in dynamo
        response = dynamo.create_table(
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
        return "Created table in DynamoDB for your dishes! \n\n {}".format(response)

    def get_all_dishes():
        return_message = ''
        # make sure that a table exists
        if TableName not in dynamo.list_tables()["TableNames"]:
            return_message += "Database table for dishes does not exist, creating one \n"
            aws_utils.assert_table_exists()

        # return a list of all table items
        return return_message + str(dynamo.scan(TableName=TableName)["Items"])

    def add_dish(dish_name):
        # check if dish exists if no, return "dish already exists". if yes, return "removed <dish>"
        return_message = ''
        # make sure that a table exists
        if TableName not in dynamo.list_tables()["TableNames"]:
            return_message += "Database table for dishes does not exist, creating one \n"
            aws_utils.assert_table_exists()

        # add / update the item in dynamodb
        dynamo.update_item(
            TableName=TableName, 
            Key= {
                'Dish': {"S": dish_name}
                }
            )

        return return_message + "Added {} to the database!".format(dish_name)

    def remove_dish(dish_name):
        # make sure a table exists in database
        if TableName not in dynamo.list_tables()["TableNames"]:
            return "Table does not exist in the Database, nothing to remove"

        # check is dish exists. if no return error if yes, return "removed <dish> from database"
        if (aws_utils.get_dish(dish_name) == None):
            return "Dish {} does not exist!".format(dish_name)

        # now we know that dish exists, we can remove
        dynamo.delete_item(
            TableName=TableName, 
            Key=aws_utils.get_dish(dish_name)
            )
        return "Removed {} from table".format(dish_name)

    def get_dish(dish_name):
        # query for the dish name, if it exists in the database, it will showup
        query = dynamo.query(
            TableName=TableName,
            KeyConditionExpression="Dish = :Dish",
            ExpressionAttributeValues = {
                    ":Dish": {'S': dish_name}
                }
        )
        # if the dish does not exist, return None
        if query["Items"] == []:
            return None
        return query["Items"][0]

    def clear_table():
        # scan the table, and delete each item 1 by 1
        items = dynamo.scan(TableName=TableName)["Items"]
        for item in items:
            dynamo.delete_item(TableName=TableName, Key=item)
        return "Cleared everything in the Database"
