import twilioRestClient
account_sid=“ACc5899cfa57cdf1054f654b65277b98e8”
auth_token=“”
client=TwilioRestClient(account_sid,auth_token)
client=TwilioRestClient(account_sid,auth_token)
message=client.sms.message.create(
body=“Hello”
to=“+1”
from=”+1513”)
print message.sid
