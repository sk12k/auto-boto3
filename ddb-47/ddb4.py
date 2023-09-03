###############################################
### Write Data to the Table as a batch process
###############################################
import boto3 
import json 
import datetime 
import uuid

# Create a DynamoDB Resource
dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table('Users')

# Generate some random data
with table.batch_writer() as user_data:
    for i in range(100): 
      user_data.put_item(
          Item={
              'user_id': str(uuid.uuid4()),
              'user_email': 'someone' + str(i) + '@somewhere.com', 
              'user_fname': 'User' + str(i),
              'user_lname': 'UserLast' + str(i)
          } 
      )
      print('Writing record # ' + str(i+1) + ' to DynamoDB Users Table') 
    print('Done!')

