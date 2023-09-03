###############################################
### look up a user in the Amazon DynamoDb Table
###############################################
import boto3
from boto3.dynamodb.conditions import Key 
import json
import datetime

# Create a DynamoDB Resource
dynamodb_resource = boto3.resource('dynamodb') 
table = dynamodb_resource.Table('Users')

# Query a some data 
response = table.query(
    KeyConditionExpression=Key('user_id').eq('1234-5679') 
)

# Print the data out!
print(json.dumps(response['Items'], indent=2, sort_keys=True))