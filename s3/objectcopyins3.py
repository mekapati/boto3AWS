# copying single object from one bucket to other bucket 
import boto3 

# Creating S3 Resource From the boto3
s3 = boto3.resource('s3') 

# create a source dicitionary that specifies bucket name and key name of the object 
copy_source = {
    'Bucket' : 'service-catalog1',
    'Key'    : 'ec2.yaml'
} 

# target bucket 
bucket = s3.Bucket('gnvsai.zemosodiagnostics.gq')

# copy object to target bucket 
bucket.copy(copy_source, 'replaceEC2.yaml')  



# copying all objects from one bucket to other bucket 
import boto3 

# create a S3 resource
s3 = boto3.resource('s3') 

# set the source and destination bucket 
src_bucket_name = 'service-catalog1'
dst_bucket_name = 'gnvsai.zemosodiagnostics.gq' 

# get the source and destination buvkets 
src_bucket = s3.Bucket(src_bucket_name)
dst_bucket = s3.Bucket(dst_bucket_name) 

# iterate through each object in the source bucket and copy it to the destination bucket 
for obj in src_bucket.objects.all(): 
    # print (obj)
    dst_bucket.copy({"Bucket": src_bucket_name, "Key": obj.key}, obj.key)

print(type(src_bucket))
