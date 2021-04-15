import smtplib, ssl
from email.message import EmailMessage

def emailsender():
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender = "cs321testgroup3@gmail.com"
	print("Default email is cs321testgroup3@gmail.com")
	receiver = input("Enter the email address of the receiving party: ")
	message = EmailMessage()
	message['Subject'] = input("Subject of your email: ")
	message['From'] = sender
	message['To'] = receiver
	message.set_content(input("Main Message: "))
	password = input("Type your password and press enter: ")
	
	context = ssl.create_default_context()
	try:
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender, password)
			server.send_message(message)
	except Exception as e:
		print(e)
