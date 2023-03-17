from twilio.rest import Client

account_sid = 'ACe6490eed28972d424c82ed31132d1755'
auth_token = '211a2952d250edcb9e832cd8b09d2884'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+886908383685'
)

print(message.sid)