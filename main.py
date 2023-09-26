from email.email_address import EmailAddress
from email.sender_mail import SenderMail
from email.priority_email import PriorityEmail

def send_email(email):
    email.send()

def run():
    
    email = EmailAddress("jhon.doe@example.com","jhanne.doe@example.com","Email Test","Hello")
    
    sender = SenderMail()
    
    priority_m = PriorityEmail()
    
    email.send(sender)
    
    priority_m.set_priority(email,"High")
    
    email.send(sender)
     
if __name__ == "__main__":
    
    run()

