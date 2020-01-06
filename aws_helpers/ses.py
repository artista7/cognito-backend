import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# boto3.setup_default_session(profile_name='vivek-us-east-1')
client = boto3.client('ses',  region_name='us-east-1')
# SOURCE_EMAIL = "notifications@learning-sage.com"
SOURCE_EMAIL = '"Shubham Gupta" <shubham.gupta@learning-sage.com>'

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
                'Html': {
                    'Data': body,
                    'Charset': 'UTF-8'
                }
            }
        },
        ReplyToAddresses=[SOURCE_EMAIL]
    )
    return response



def send_raw_email(to_address, subject, body):
    # Create a multipart/mixed parent container.
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = subject 
    msg['From'] = SOURCE_EMAIL 
    # msg['To'] = to_address
    msg['Bcc'] = to_address

    CHARSET = 'utf-8'

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    htmlpart = MIMEText(body.encode(CHARSET), 'html', CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(htmlpart)


    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)

    try:
        #Provide the contents of the email.
        response = client.send_raw_email(
            Source=SOURCE_EMAIL,
            Destinations=
                to_address.split(',')
            ,
            RawMessage={
                'Data':msg.as_string(),
            },
        )
    except Exception as e:
        print(response['Error']['Message'])
    
    return response
