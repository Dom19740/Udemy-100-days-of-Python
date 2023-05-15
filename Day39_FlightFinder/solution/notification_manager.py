from twilio.rest import Client

TWILIO_SID = 'ACa3c015cc5e6c0bfd001db9f617d88b1b'
TWILIO_AUTH_TOKEN = '00f095ba6e39ef5fb3a84bba66e053b4'
TWILIO_VIRTUAL_NUMBER = '+12708125618'
TWILIO_VERIFIED_NUMBER = '+34652678183'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
