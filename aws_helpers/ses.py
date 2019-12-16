import boto3

boto3.setup_default_session(profile_name='vivek-us-east-1')
client = boto3.client('ses',  region_name='us-east-1')
SOURCE_EMAIL = "notifications@learning-sage.com"


def send_email(to_address, subject, body):
    to_address = [to_address] if type(to_address) == str else to_address
    response = client.send_email(
        Source=SOURCE_EMAIL,
        Destination={
            'ToAddresses': to_address
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': body,
                    'Charset': 'UTF-8'
                }
            }
        },
        ReplyToAddresses=[SOURCE_EMAIL]
    )
    return response

