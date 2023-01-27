import boto3 

# connect to SES 
ses = boto3.client('ses') 

# Define the email parameters 
recipient = "malyadri.mekapati@zemosolabs.com"
sender = "malyadrinaidu90@gmail.com"
subject = "Testing AWS SES with boto3 resource"
body = "This is a test email sent using boto3 and AWS SES resources."

# send the email 
response = ses.send_email(
  Destination = {
    'ToAddresses' : [
        recipient,
    ],
  },
  Message = {
    'Body' : {
        'Text' : {
            'Charset': 'UTF-8',
            'Data': body,
        }, 
    }, 
    'Subject' : {
        'Charset' : 'UTF-8',
        'Data': subject,
    }, 
 },
    Source = sender, 
)   

print (response)


# import boto3
# from botocore.exceptions import ClientError

# def send_email():
#     SENDER = "malyadrinaidu90@gmail.com" # must be verified in AWS SES Email
#     RECIPIENT = "malyadri.mekapati@zemosolabs.com" # must be verified in AWS SES Email


#     # The subject line for the email.
#     SUBJECT = "This is test email for testing purpose..!!"

#     # The email body for recipients with non-HTML email clients.
#     BODY_TEXT = ("Hey Hi..."
#                 "This email was sent with Amazon SES using the "
#                 "AWS SDK for Python (Boto)."
#                 )
                
#     # The HTML body of the email.
#     BODY_HTML = """<html>
#     <head></head>
#     <body>
#     <h1>Hey Hi...</h1>
#     <p>This email was sent with
#         <a href='https://aws.amazon.com/ses/'>Amazon SES CQPOCS</a> using the
#         <a href='https://aws.amazon.com/sdk-for-python/'>
#         AWS SDK for Python (Boto)</a>.</p>
#     </body>
#     </html>
#                 """            

#     # The character encoding for the email.
#     CHARSET = "UTF-8"

#     # Create a new SES resource and specify a region.
#     client = boto3.client('ses',region_name=AWS_REGION)

#     # Try to send the email.
#     try:
#         #Provide the contents of the email.
#         response = client.send_email(
#             Destination={
#                 'ToAddresses': [
#                     RECIPIENT,
#                 ],
#             },
#             Message={
#                 'Body': {
#                     'Html': {
        
#                         'Data': BODY_HTML
#                     },
#                     'Text': {
        
#                         'Data': BODY_TEXT
#                     },
#                 },
#                 'Subject': {

#                     'Data': SUBJECT
#                 },
#             },
#             Source=SENDER
#         )
#     # Display an error if something goes wrong.	
#     except ClientError as e:
#         print(e.response['Error']['Message'])
#     else:
#         print("Email sent! Message ID:"),
#         print(response['MessageId'])
