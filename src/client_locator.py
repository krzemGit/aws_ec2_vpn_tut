import boto3
from src.aws_keys import AWS_SECRET_KEY, AWS_ACCESS_KEY

class ClientLocator:
    def __init__(self, client):
        self._client = boto3.client(
            client,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name='eu-central-1'
            )

    def get_client(self):
        return self._client

class EC2Client(ClientLocator):
    def __init__(self):
        super().__init__('ec2')
