import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Specify the bucket name and object (file) details
bucket_name = 'sk-test-boto-bucket'
object_key = 'test.jpg'  # Object (file) key in the bucket
file_path = 'test.jpg'  # Path to the file you want to upload

# Create an S3 bucket
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"S3 bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Error creating S3 bucket '{bucket_name}': {e}")

# Upload an object to the bucket
try:
    s3.upload_file(file_path, bucket_name, object_key)
    print(f"Object '{object_key}' uploaded to bucket '{bucket_name}' successfully.")
except Exception as e:
    print(f"Error uploading object '{object_key}' to bucket '{bucket_name}': {e}")
