import boto3 


def lambda_handler(event, conetxt): 
    client = boto3.client('sns') 
    topic_arn = 'arn:aws:sns:us-east-2:365299945243:boto3-lambda' 
    message = 'Ec2 instances has been stopped'
    client.publish(TopicArn = topic_arn,Message = message)  