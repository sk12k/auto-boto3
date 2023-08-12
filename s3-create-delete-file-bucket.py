import boto3

bucket_name = 'sk-boto3-test-create'
file_key = 'test.jpg'

# Create an S3 client
s3 = boto3.client('s3')


# Delete the file
try:
    s3.delete_object(Bucket=bucket_name, Key=file_key)
    print(f"File '{file_key}' deleted successfully from bucket '{bucket_name}'.")
except Exception as e:
    print(f"Error deleting file '{file_key}' from bucket '{bucket_name}': {e}")

# Delete the bucket
try:
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")
except Exception as e:
    print(f"Error deleting bucket '{bucket_name}': {e}")


# # Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)