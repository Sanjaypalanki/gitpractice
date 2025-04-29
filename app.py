import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2', region_name='us-east-1')  # Change region as needed

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0c94855ba95c71c99',  # Amazon Linux 2 AMI (example for us-east-1)
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-pair-name',  # Replace with your actual key pair name
    SecurityGroupIds=['sg-0123456789abcdef0'],  # Replace with your security group ID
    SubnetId='subnet-0123456789abcdef0',        # Replace with your subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyPythonInstance'}]
        }
    ]
)

#print(f"EC2 Instance '{instances[0].id}' launched successfully.")

