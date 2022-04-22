import boto3
import pprint

Email = 'test@test.com'
Password = 'Test@3601'
client = boto3.client('cognito-idp', region_name='ap-south-1')
response = client.initiate_auth(
    ClientId='53cnie8g86gldjrg3hsknbuhck',
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': Email,
        'PASSWORD': Password
    }
)
pprint.pprint(response)

