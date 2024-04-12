import boto3
import os
from config_parser import fetch_config

config_path = os.environ.get("CONFIG_PATH")
config = fetch_config(config_path)

def extract_bucket_key_and_filename(s3_uri):
    # Remove the 's3://' prefix
    s3_uri = s3_uri.replace('s3://', '')

    # Split the string by the first occurrence of '/'
    parts = s3_uri.split('/', 1)

    # The first part will be the bucket name and the second part will be the key with filename
    bucket_name = parts[0]
    key_with_filename = parts[1] if len(parts) > 1 else ''

    # Split the key with filename by the last occurrence of '/'
    filename_parts = key_with_filename.rsplit('/', 1)

    # The last part will be the filename and the remaining part will be the key
    if len(filename_parts) > 1:
        key = filename_parts[0]
        filename = filename_parts[1]
    else:
        key = ''
        filename = filename_parts[0]

    return bucket_name, key, filename


async def download_csv_from_s3(bucket_name=None,topic_name=None):
    aws_access_key_id = config['AWS']['AWS_ACCESS_KEY_ID']
    aws_secret_access_key =  config['AWS']['AWS_SECRET_ACCESS_KEY']
    # Create S3 client
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    setapath=f'resources/{topic_name}_seta.csv'
    setbpath=f'resources/{topic_name}_setb.csv'
    
    try:
        # Upload the file
        response = s3_client.download_file(bucket_name, f"{topic_name}_questions_and_answers_seta.csv", setapath)
        response = s3_client.download_file(bucket_name, f"{topic_name}_questions_and_answers_setb.csv", setbpath)

        return "success"
    except Exception as e:
        print(f"Failed to upload file to S3: {e}")