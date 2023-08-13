import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify the instance ID to terminate

# instance_id_to_terminate = 'i-xxxxxxxxxxxxxxxxx'  # Replace with the actual instance ID
instance_id_to_terminate = 'i-084c3bcd69f17ce74'  # Replace with the actual instance ID

# Terminate the EC2 instance
try:
    ec2.terminate_instances(InstanceIds=[instance_id_to_terminate])
    print(f"EC2 instance '{instance_id_to_terminate}' terminated successfully.")
except Exception as e:
    print(f"Error terminating EC2 instance '{instance_id_to_terminate}': {e}")
