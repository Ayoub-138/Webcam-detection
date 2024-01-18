import  os, smtplib, imghdr
import time
from email.message import EmailMessage

SENDER = "ayoub.ayadi.138@gmail.com"
PASSWORD = os.getenv("PASSWORD")
RECEIVER = "ayoub.ayadi.138@gmail.com"
HOST = "smtp.gmail.com"
PORT = 587


def send_email(img_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Movement detected"
    email_message.set_content("Camera detected  movement on the screen")

    with open(img_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP(HOST, PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    time.sleep(15)

if __name__ == "__main__":
    send_email(img_path="images/19.png")

