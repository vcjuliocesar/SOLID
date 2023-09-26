#from sender_mail import SenderMail
#from email_manager import EmailManager
class EmailAddress:
    
    def __init__(self,sender:str,addressee:str,subject:str,body:str) -> None:
        
        self.sender = sender
        
        self.addressee = addressee
        
        self.subject = subject
        
        self.body = body
        
        self.priority = "Normal"
    
    # def set_sender(self,sender:str):
        
    #     self.sender = sender
    
    # def set_addressee(self,addresse:str):
        
    #     self.addressee = addresse
    
    # def set_subject(self,subject:str):
        
    #     self.subject = subject
    
    # def set_body(self,body:str):
        
    #     self.body = body
    
    def send(self,email_manager):
        
        email_manager.send(self)
        #print(f"Email sent from {self.sender} to {self.addressee} with subject {self.subject}")
        
        #raise NotImplementedError