import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(bucket_name, s3_key, file_path):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_path} uploaded to {bucket_name} as {s3_key}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found")
    except NoCredentialsError:
        print("Credentials not available")

# Add more S3 related helper functions as needed.
