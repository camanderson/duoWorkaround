from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC136c27d243f697f5b31270917024f879"
# Your Auth Token from twilio.com/console
auth_token  = "7b9530de53f35a007881f7128c20de5f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14406662666", 
    from_="+16149074552",
    body="Hello from Python!")

print(message.sid)