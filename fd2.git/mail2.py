import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

my_sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

# Change to your verified sender
from_email = Email("22eg105n64@anurag.edu.in")  

# Change to your recipient
to_email = To("cmsh800@gmail.com")  

subject = "Lorem ipsum dolor sit amet"
content = Content("text/plain", "consectetur adipiscing elit")

mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = my_sg.client.mail.send.post(request_body=mail_json)