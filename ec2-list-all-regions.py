import boto3

# Replace these with your AWS credentials
# aws_access_key = 'YOUR_AWS_ACCESS_KEY'
# aws_secret_key = 'YOUR_AWS_SECRET_KEY'

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get a list of all available regions
all_regions = ec2.describe_regions()

# Iterate through each region and list instances
for region in all_regions['Regions']:
    region_name = region['RegionName']
    print(f"Instances in region: {region_name}")
    
    # Create a new EC2 client for the specific region
    region_ec2 = boto3.client('ec2')
    
    # Describe instances in the region
    instances = region_ec2.describe_instances()
    
    # Print instance details
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            print(f"Instance ID: {instance_id}, State: {instance_state}")
    
    print('\n')
