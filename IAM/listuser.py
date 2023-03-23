import json
import boto3
from botocore.exceptions import ClientError 

def list_iam_users():
    try:
        iam_client = boto3.client('iam')
        paginator = iam_client.get_paginator('list_users')
        for response in paginator.paginate():
            #print(response["Users"])
            for user in response["Users"]:
                print("User name: ",user["UserName"])
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)
    
list_iam_users()  