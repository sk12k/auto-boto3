##########################################
### Add users to the Amazon DynamoDb Table
##########################################
import boto3
import json
import datetime
# Create a DynamoDB Resource
dynamodb_resource = boto3.resource('dynamodb') 
table = dynamodb_resource.Table('Users')

# Write a record to DynamoDB 
response = table.put_item(
  Item={
    'user_id': '1234-5679',
    'user_email': 'someone@somewhere.com', 
    'user_fname': 'John',
    'user_lname': 'Smith'
  } 
)
# Just printing the raw JSON response, you should see a 200 status code 
print(json.dumps(response, indent=2, sort_keys=True))