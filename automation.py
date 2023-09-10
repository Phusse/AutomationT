import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Email configuration
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'
    recipient_email = 'recipient_email@gmail.com'
    subject = 'Automation Test'
    message_body = 'This is a test email sent via automation.'

    # Create a MIME object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message_body, 'plain'))

    # Establish a connection with the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to your Gmail account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Quit the server
    server.quit()
    print('Email sent successfully!')

if __name__ == '__main__':
    send_email()
