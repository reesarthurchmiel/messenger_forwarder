import os

from twilio.rest import Client

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
    phone_number_to = os.environ['TWILIO_DESTINATION_PHONE_NUMBER']
except:
    print("Please specify TWILIO_DESTINATION_PHONE_NUMBER in twilio.env, and source twilio.env")
    exit(-1)

try:
    phone_number_from = os.environ['TWILIO_ACCOUNT_PHONE_NUMBER']
except:
    print("Please specify TWILIO_ACCOUNT_PHONE_NUMBER in twilio.env, and source twilio.env")
    exit(-1)

client = Client(account_sid, auth_token)

def send_sms(text):
    client.messages \
            .create(
                 body=text,
                 from_=phone_number_from,
                 to=phone_number_to
             )


if __name__ == "main":
    send_sms("This is a test!")
