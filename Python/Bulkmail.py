import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, body, smtp_server, smtp_port, login, password):
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(login, to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")

def send_bulk_emails(recipient_list, subject, body, smtp_server, smtp_port, login, password):
    for recipient in recipient_list:
        send_email(recipient, subject, body, smtp_server, smtp_port, login, password)

# Define email details
subject = "Hi, good morning everyone!!!"
body = "This is a test email sent in bulk."
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "yourmail"
password = "google mail app passwd" 

# List of recipient emails
recipient_list = [
    "add recipient mail" 
]

# Send the emails
send_bulk_emails(recipient_list, subject, body, smtp_server, smtp_port, login, password)
