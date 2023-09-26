from sender_mail import SenderMail

class EmailAddress(SenderMail):
    
    def __init__(self) -> None:
        
        self.sender = ""
        
        self.addressee = ""
        
        self.subject = ""
        
        self.body = ""
    
    def set_sender(self,sender:str):
        
        self.sender = sender
    
    def set_addressee(self,addresse:str):
        
        self.addressee = addresse
    
    def set_subject(self,subject:str):
        
        self.subject = subject
    
    def set_body(self,body:str):
        
        self.body = body
    
    def send(self):
        
        print(f"Email sent from {self.sender} to {self.addressee} with subject {self.subject}")
        
        #raise NotImplementedError