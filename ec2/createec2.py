import boto3 

ec2 = boto3.resource('ec2')

security_group = ec2.create_security_group(
    GroupName = 'my_security_group',
    Description = 'my security group'
)
security_group.authorize_ingress(
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort' : 22,
            'ToPort'   : 22,
            'IpRanges' : [{'CidrIp':'0.0.0.0/0'}] 
        },
        {
            'IpProtocol': 'tcp',
            'FromPort' : 80,
            'ToPort'   : 80,
            'IpRanges' : [{'CidrIp':'0.0.0.0/0'}] 
        }
    ]
) 

instance = ec2.create_instances(
    ImageId = 'ami-097a2df4ac947655f',
    InstanceType = 't2.micro',
    MinCount = 1,
    MaxCount = 1,
    SecurityGroupIds = [security_group.id],
    KeyName = 'mykeypair',
    TagSpecifications=[{'ResourceType': 'instance', 
                         'Tags': [
                            {
                                'Key': 'name',
                                'Value': 'boto3'
                            },
                         ] 
                     },
                  ],
)
