import boto3 

s3 = boto3.client('s3') 

# list of buckets 
response = s3.list_buckets() 
for bucket in response['Buckets']: 

 print(bucket['Name'])   
 
 

# delete object in bucket  
bucket_name = 'gnvsai.zemosodiagnostics.gq' 
object_key = 'sample.yaml'

response = s3.delete_object(Bucket=bucket_name,Key=object_key) 

print(response) 