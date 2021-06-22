import boto3, botostubs

class VPC:
    def __init__(self, client):
        self._client = client

    def create_vpc(self):
        print('Creating a vpc')
        return self._client.create_vpc(
            CidrBlock="10.0.0.0/16"
        )

    def add_name_tag(self, resource_id, resource_name):
        print(f'Adding name {resource_name} to vpc {resource_id}')
        return self._client.create_tags(
            Resource=[resource_id],
            Tags=[{
                'Key': 'Name',
                'Value': resource_name
            }]
        )

    def create_internet_gateway(self):
        print("Creating internet gateway...")
        return self._client.create_internet_gateway()

    def attach_igw_to_vpc(self, vpc_id, igw_id):
        print(f'Attaching internet gateway {igw_id} to vpc {vpc_id}')
        return self._client.attach_internet_gateway(
            InternetGatewayId=igw_id,
            VpcId=vpc_id
        )

    def create_subnet(self, vpc_id, cidr_block):
        print(f'Creating subnet for {vpc_id} with cidr block {cidr_block}')
        return self._client.create_subnet(
            VpcId=vpc_id,
            CidrBlock=cidr_block
        )

    def create_public_route_table(self, vpn_id):
        print(f'Creating public route table for VPN {vpn_id}')
        return self._client.create_route_table(VpnId=vpn_id)

    def create_igw_route_to_public_route_table(self, rtb_id, vpc_id):
        print(f"Creating GATEWAY route for {rtb_id} to Route Table for VPC {vpc_id}")
        return self._client.create_route(
            RouteTableId=rtb_id,
            VpcId=vpc_id,
            DestinationCidrBlock='0.0.0.0/0'
        )