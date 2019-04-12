import os

#from twilio.rest import Client
import twilio

try:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
except:
    print("Please specify TWILIO_ACCOUNT_SID in twilio.env, and source twilio.env")
    exit(-1)

try:
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
except:
    print("Please specify TWILIO_AUTH_TOKEN in twilio.env, and source twilio.env")
    exit(-1)

try:
    phone_number = os.environ['TWILIO_DESTINATION_PHONE_NUMBER']
except:
    print("Please specify TWILIO_DESTINATION_PHONE_NUMBER in twilio.env, and source twilio.env")
    exit(-1)

#client = Client(account_sid, auth_token)
print(phone_number)