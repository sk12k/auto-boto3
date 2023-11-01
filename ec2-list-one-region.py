import boto3

def list_ec2_instances(region_name):
    ec2_client = boto3.client('ec2', region_name=region_name)

    try:
        response = ec2_client.describe_instances()
        instances = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance)

        return instances

    except Exception as e:
        print("Error:", e)
        return []

def main():
    region_name = 'us-east-1'  # Change this to your desired region

    instances = list_ec2_instances(region_name)

    for instance in instances:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']
        private_ip = instance.get('PrivateIpAddress', 'N/A')
        public_ip = instance.get('PublicIpAddress', 'N/A')

        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_type}")
        print(f"State: {state}")
        print(f"Private IP: {private_ip}")
        print(f"Public IP: {public_ip}")
        print("=" * 30)

if __name__ == '__main__':
    main()
