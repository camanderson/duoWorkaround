from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14406662666", 
    from_="+16149074552",
    body="Hello from Python!")

print(message.sid)
