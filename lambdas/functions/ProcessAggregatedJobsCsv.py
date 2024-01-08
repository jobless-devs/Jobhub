import boto3
import urllib.parse

def lambda_handler(event, context):
    # Initialize Boto3 client for Glue
    glue_client = boto3.client('glue')

    # Extract bucket name and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    # Construct the S3 path
    s3_path = f"s3://{bucket}/{key}"

    glue_job_name = 'jobhub-glue-s3-to-rds'

    # Start the Glue job with the S3 path as an argument
    response = glue_client.start_job_run(
        JobName=glue_job_name,
        Arguments={
            '--S3_PATH': s3_path  # Passing S3_PATH argument to Glue script
        }
    )

    return {
        'statusCode': 200,
        'body': f"Glue job {glue_job_name} started with S3 path: {s3_path}",
        'response': response
    }
