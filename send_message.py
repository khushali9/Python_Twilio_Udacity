from twilio.rest import TwilioRestClient
account_sid="***"
auth_token="***"
client=TwilioRestClient(account_sid,auth_token)
message=client.sms.messages.create(body="Hello Khushali", to="+1your_no" ,from_="+1twilio_no")
print message.sid
