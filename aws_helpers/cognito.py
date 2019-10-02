import os
import boto3
import random
import string
boto3.setup_default_session(profile_name='vivek-us-east-1')
client = boto3.client('cognito-idp')

COGNITO_USER_POOL = os.environ["COGNITO_USER_POOL"]


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def create_new_user(email, name, phone_number, group, instituteName):
    response = client.admin_create_user(
        UserPoolId=COGNITO_USER_POOL,
        Username="{}_{}".format(group, email),
        UserAttributes=[i for i in [
            {
                'Name': 'email',
                'Value': email,
            },        {
                'Name': 'name',
                'Value': name,
            },        {
                'Name': 'phone_number',
                'Value': phone_number,
            },        {
                'Name': 'custom:group',
                'Value': group,
            },        {
                'Name': 'custom:collegeName',
                'Value': str(instituteName) if group == "college" else None,
            },        {
                'Name': 'custom:companyName',
                'Value': str(instituteName) if group == "company" else None,
            }
        ] if i['Value']],
        TemporaryPassword=randomString(),
        DesiredDeliveryMediums=[
            'SMS', 'EMAIL',
        ],
    )
    return response


def block_user(username):
    response = client.admin_disable_user(
        UserPoolId=COGNITO_USER_POOL,
        Username=username
    )
    return response


def unblock_user(username):
    response = client.admin_enable_user(
        UserPoolId=COGNITO_USER_POOL,
        Username=username
    )
    return response
