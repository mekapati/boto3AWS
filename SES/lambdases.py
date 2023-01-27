import boto3 

def lambda_handler(event,conetxt): 
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

    return response['MessageId']