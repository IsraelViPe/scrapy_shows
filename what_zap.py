import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

twilio_sandbox = "whatsapp:+14155238886"


def send_whatzap(remetents, text):
    for remetent in remetents:
        client.messages.create(from_=twilio_sandbox, body=text, to=remetent)
