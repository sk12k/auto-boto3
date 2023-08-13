import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify the instance parameters
instance_params = {
    'ImageId': 'ami-08a52ddb321b32a8c',   # Replace with the desired AMI ID
    'InstanceType': 't2.micro',           # Replace with the desired instance type
#   'KeyName': 'your-key-pair-name',      # Replace with your key pair name (if needed)
    'MinCount': 1,
    'MaxCount': 1
}

# Create the EC2 instance
try:
    instances = ec2.run_instances(**instance_params)
    instance_id = instances['Instances'][0]['InstanceId']
    print(f"EC2 instance '{instance_id}' created successfully.")
except Exception as e:
    print(f"Error creating EC2 instance: {e}")
