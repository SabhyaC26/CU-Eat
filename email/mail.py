import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "cuswiperight@gmail.com"
receiver_email = "sabhyachhabria@gmail.com"
password = input("Type your password and press enter: ")


message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the HTML version of your message
html = """\
<html>
  <body>
    <p>Hi Sabhya, <br>
      How are you? <br>
      Your favorite dish PASTA! is available at Cook House Dining Hall
    </p>
    <p>Find out more here!<br>
       <a href="https://now.dining.cornell.edu/eateries">Cornell Dining</a>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
main = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(main)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
