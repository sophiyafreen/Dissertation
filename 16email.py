import smtplib
import ssl
from email.message import EmailMessage
from email.utils import make_msgid
from getpass import getpass


subject = input("Enter a subject: ")
body = input("Enter a body: ")
image = body = input("Enter a path to an image file: ")
sender_email = input("Enter a sender: ")
reciever_email = input("Enter a reciever(separate the addresses with ' '): ")
reciever_email = reciever_email.split()
password = getpass()

message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject
img_cid = make_msgid()

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <img src="cid: {img_cid}">
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

with open(image, 'rb') as img:
    message.get_payload()[0].add_related(img.read(), 'image', 'jpeg', cid=img_cid)

with open('outgoing.message', 'wb') as f:
    f.write(bytes(message))

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string())

print("Success")