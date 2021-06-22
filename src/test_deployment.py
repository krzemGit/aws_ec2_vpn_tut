from src.ec2.vpc import VPC
from src.client_locator import EC2Client

def main():
    # Create a VPC
    ec2_client = EC2Client().get_client()
    vpc = VPC(ec2_client)

    vpc_response = vpc.create_vpc()

    print('VPC Created' + str(vpc_response))

    # add name to the vpn
    vpc_name = "Boto3-VPC"
    vpc_id = vpc_response['Vpc']['VpcId']
    vpc.add_name_tag(vpc_id, vpc_name)
    print(f'Added {vpc_name} to {vpc_id}')

    # create internet gateway
    igw_response = vpc.create_internet_gateway()
    igw_id = igw_response['InternetGateway']['InternetGatewayId']

    # attach IGW to VPC
    vpc.attach_igw_to_vpc(vpc_id, igw_id)

    # creating subnet
    public_subnet_response = vpc.create_subnet(vpc_id, '10.0.1.0/24')
    print(f'Creating subnet for {vpc_id} : {str(public_subnet_response)}')

    #creating public route table
    public_route_table_response = vpc.create_public_route_table(vpc_id)
    print('Created public route table')

    rtb_id = public_route_table_response['RouteTable']['RouteTableId']

    # Adding IGW to Public route table
    vpc.create_igw_route_to_public_route_table(rtb_id, igw_id)

if __name__ == "__main__":
    main()