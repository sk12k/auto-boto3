####################################
### remove the Amazon DynamoDb Table
####################################

import boto3 
import json 
import datetime 
import uuid

# Create a DynamoDB Resource 
dynamodb_client = boto3.client('dynamodb')

# Delete the Table
response = dynamodb_client.delete_table(TableName='Users') 
print(json.dumps(response, indent=2, sort_keys=True))