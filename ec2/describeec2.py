import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances(InstanceIds=['i-037871189d8047ff7'])

print(response)
