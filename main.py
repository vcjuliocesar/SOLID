from email_address import EmailAddress
from priority_email import PriorityEmail

def run():
    
    email = EmailAddress()
    # email.set_sender("test@test.com")
    # email.set_addressee("jhon.doe@test.com")
    # email.set_subject("Email Test")
    # email.set_body("Hello")
    # email.send()
    
    priority = PriorityEmail()
    priority.set_sender("test@test.com")
    priority.set_addressee("jhon.doe@test.com")
    priority.set_subject("Email Test Priority")
    priority.set_body("Hello")
    priority.set_priority("High")
    priority.send()
    
if __name__ == "__main__":
    
    run()