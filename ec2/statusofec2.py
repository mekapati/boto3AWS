# import boto3 

# ec2 = boto3.resource('ec2')  

import boto3 

EC2_RESOURCE = boto3.resource('ec2')  
instance_type = 'running'   
# instances = EC2_RESOURCE.instances.all()  

instances = EC2_RESOURCE.instances.filter(
      Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                instance_type
            ]
        }
    ]
)

for instance in instances:
    print(f'EC2 instance {instance.id} information:')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance AMI: {instance.image.id}')
    print(f'Instance platform: {instance.platform}')
    print(f'Instance type: "{instance.instance_type}')
    print(f'Public IPv4 address: {instance.public_ip_address}')
    print('-'*30)