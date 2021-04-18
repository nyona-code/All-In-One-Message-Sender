import smtplib, ssl
from email.message import EmailMessage

def gmail(r_address, subject, msg):
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender = "cs321testgroup3@gmail.com"
	password = "Pass!word"
	receiver = r_address
	message = EmailMessage()
	message['Subject'] = subject
	message['From'] = sender
	message['To'] = receiver
	message.set_content(msg)
	
	context = ssl.create_default_context()
	try:
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender, password)
			server.send_message(message)
	except Exception as e:
		print(e)
