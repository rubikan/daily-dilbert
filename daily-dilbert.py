import email
import json
import os
import requests
import smtplib
import ssl
from bs4 import BeautifulSoup
from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = "dilbert.gif"

def download_comic():
    page_url = "https://dilbert.com/strip/" + date.today().strftime('%Y-%m-%d')
    page_resp = requests.get(page_url)
    soup = BeautifulSoup(page_resp.text, "html.parser")
    image_tag = soup.find('img', {'class': 'img-comic'})     
    img_url = "https:" + image_tag.get("src")
    img_resp = requests.get(img_url, allow_redirects=True)
    open(filename, "wb").write(img_resp.content)

def send_mails(config):
    host = config["HOST"]
    port = config["PORT"]
    username = config["USER"]
    password = config["PASS"]  

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = username
    message["Subject"] = "Daily Dilbert " + date.today().strftime('%d.%m.%Y')

    # Add body to email
    message.attach(MIMEText("Viel Spaß!", "plain"))

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message
    message.attach(part)

    # Create a secure SSL context
    context = ssl.create_default_context()    

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        for rec in config["RECIPIENTS"]:
            message["To"] = rec
            text = message.as_string()
            server.sendmail(username, rec, text)

with open('config.json', 'r') as f:
    config = json.load(f)

download_comic()
if "MAIL" in config:
    send_mails(config["MAIL"])
os.remove(filename)