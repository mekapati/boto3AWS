import boto3 
# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all(): 
    print(bucket.name) 

# upload a file 
data = open('sample.yaml')
s3.Bucket('service-catalog1').put_object(Key='sample.yaml', Body=data)    