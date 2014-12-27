import twilioRestClient
account_sid=“your sid pls”
auth_token=“your token pls”
client=TwilioRestClient(account_sid,auth_token)

message=client.sms.message.create(
body=“Hello”,
to=“+1”,
from_=”+1513”)
print message.sid
