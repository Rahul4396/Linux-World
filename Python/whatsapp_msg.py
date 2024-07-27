pip install pywhatkit
import smtplib


import pywhatkit as kit

# Specify the recipient's phone number (including country code, e.g., +1234567890)
phone_number = 'enter recipient number'

# Specify the message to send
message = 'hlooo'

# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)
