import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AWS-ACCESS-KEY-ID'
ACCESS_SECRET_KEY = 'AWS-ACCESS-SECRET-KEY'
BUCKET_NAME = 'S3_BUCKET-NAME'

data = open('File-Name', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='File-Name', Body=data)

print ("File Uplaoded to S3 Bucket Successfully")