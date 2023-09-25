from email_address import EmailAddress

def run():
    
    email = EmailAddress()
    email.set_sender("test@test.com")
    email.set_addressee("jhon.doe@test.com")
    email.set_subject("Email Test")
    email.set_body("Hello")
    email.set_send()
    
if __name__ == "__main__":
    
    run()