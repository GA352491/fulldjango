from pycognito import Cognito

u = Cognito('ap-south-1_naR1NxJe2', '53cnie8g86gldjrg3hsknbuhck', username='test@test.com')
u.authenticate(password='Test@3601')
# print(u.id_token)

u2 = Cognito('ap-south-1_naR1NxJe2', '53cnie8g86gldjrg3hsknbuhck',
             id_token=u.id_token, refresh_token=u.refresh_token,
             access_token=u.access_token)
u2.verify_tokens()
