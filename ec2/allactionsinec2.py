import boto3

ec2 = boto3.client('ec2')

# describe instances 
response = ec2.describe_instances(InstanceIds=['i-037871189d8047ff7'])
print(response)
 

# stop instances 
response = ec2.stop_instances(InstanceIds=["i-0702e7a783dc16c18"])
print(response) 

# reboot instance
response = ec2.reboot_instances(InstanceIds=["i-0702e7a783dc16c18"])
print(response)

# start instance 
response = ec2.start_instances(InstanceIds=["i-0702e7a783dc16c18"])
print(response)

# terminate single instances 
response = ec2.terminate_instances(InstanceIds=["i-0702e7a783dc16c18"])
print(response)

# terminate multiple instances 

instance_ids = ["id1","id2"] 
response = ec2.terminate_instances(InstanceIds=instance_ids) 
print(response)   