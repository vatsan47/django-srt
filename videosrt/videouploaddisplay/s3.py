import boto3
from botocore.exceptions import NoCredentialsError
import os

ACCESS_KEY = 'AKIAWZF3T2VBXVZR6V53'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    s3_file = os.path.basename(local_file)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False