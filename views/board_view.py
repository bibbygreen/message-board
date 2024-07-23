
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

load_dotenv()

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

async def upload_to_s3(file):
    try:
        file_name = file.filename
        bucket_name = os.getenv('S3_BUCKET_NAME')
        s3_client.upload_fileobj(file.file, bucket_name, file_name)
        file_url = f"https://d2g3ww52v5h2yq.cloudfront.net/{file_name}"
        return file_url
    except NoCredentialsError:
        raise Exception("Credentials not available")