import boto3 

s3 = boto3.resource('s3')

bucket_name = 'service-catalog1'
file_name = 'ec2.yaml'
local_path = '/home/malyadm/boto3AWS/ec2.yaml'

s3.Bucket(bucket_name).download_file(file_name,local_path)