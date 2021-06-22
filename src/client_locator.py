import boto3

class ClientLocator:
    def __init__(self, client):
        self._client = boto3.client(
            client,
            aws_access_key_id="AKIAU4L6DO3BFJLNG4GM",
            aws_secret_access_key= "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",
            region_name='eu-central-1'
            )

    def get_client(self):
        return self._client

class EC2Client(ClientLocator):
    def __init__(self):
        super().__init__('ec2')
