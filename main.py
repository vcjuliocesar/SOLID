from email_address import EmailAddress
from sender_mail import SenderMail
from priority_email import PriorityEmail

def send_email(email):
    email.send()

def run():
    
    email = EmailAddress("jhon.doe@example.com","jhanne.doe@example.com","Email Test","Hello")
    
    sender = SenderMail()
    
    priority_m = PriorityEmail()
    
    email.send(sender)
    
    priority_m.set_priority(email,"High")
    
    email.send(sender)
    
    # email = EmailAddress()
    # email.set_sender("test@test.com")
    # email.set_addressee("jhon.doe@test.com")
    # email.set_subject("Email Test")
    # email.set_body("Hello")
    # #email.send()
    
    # priority = PriorityEmail()
    # priority.set_sender("test@test.com")
    # priority.set_addressee("jhon.doe@test.com")
    # priority.set_subject("Email Test Priority")
    # priority.set_body("Hello")
    # priority.set_priority("High")
    # #priority.send()
    
    # send_email(email)
    # send_email(priority)
    
if __name__ == "__main__":
    
    run()