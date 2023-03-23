import json
import boto3
from botocore.exceptions import ClientError

# Create IAM User
def create_iam_user(user_name):
    try:
        iam_client = boto3.client('iam')
        response = iam_client.create_user(UserName=user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
            return False
        else:
            print("Unexpected error: %s" % e)
            return False
    return response
responseObject = create_iam_user("testboto3")
print(responseObject)

# attaching the access and secret key
client = boto3.client('iam')
access_keys = client.create_access_key(UserName="testboto3") 
print(access_keys)
# # update the userName
def update_iam_user(existing_user_name, new_user_name):
    try:
        iam_client = boto3.client('iam')
        iam_client.update_user(UserName=existing_user_name,
                            NewUserName=new_user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)
update_iam_user("boto3test", "testboto3")

# # delete the UserName 
def delete_iam_user(existing_user_name):
    try:
        iam_client = boto3.client('iam')
        iam_client.delete_user(UserName=existing_user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)
delete_iam_user("boto3test")

# # create a policy 
def create_iam_policy(policy_name, policy_json):
    try:
        iam_client = boto3.client('iam')
        iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_json)
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
            return False
        else:
            print("Unexpected error: %s" % e)
            return False
    return True

custom_policy_json = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "ec2:*"
            ],
            "Resource": "*"
        }]
    }
create_iam_policy("test_boto3", custom_policy_json)
 

# # attach a policy to user 

def attach_custom_iam_policy_with_user(policy_name, user_name):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::{account_id}:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)

attach_custom_iam_policy_with_user("test_boto3", "boto3test")    # with policy arn 

# detch a policy to user
def detach_custom_iam_policy_with_user(policy_name, user_name):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::{account_id}:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.detach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)  
detach_custom_iam_policy_with_user("test_boto3","boto3test")

