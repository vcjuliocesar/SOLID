from interfaces.email_manager import EmailManager

class SenderMail(EmailManager):
    
    def send(self,email):
        
        print(f"Email sent from {email.sender} to {email.addressee} with subject {email.subject} and priority {email.priority}")

