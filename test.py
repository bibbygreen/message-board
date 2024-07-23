import boto3
import os
from dotenv import load_dotenv

load_dotenv()

mine_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
mine_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
mine_aws_region = os.getenv('AWS_REGION')
# Initialize a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=mine_access_key_id,
    aws_secret_access_key=mine_secret_access_key,
    region_name=mine_aws_region
)

# Use the session to create an S3 client
s3 = session.client('s3')

# Upload a file
s3.upload_file('./static/pics/checked.png', 'ticket94-s3', 'your-image.jpg')

print("Upload successful!")
