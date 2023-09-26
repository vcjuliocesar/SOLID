
class EmailAddress:
    
    def __init__(self,sender:str,addressee:str,subject:str,body:str) -> None:
        
        self.sender = sender
        
        self.addressee = addressee
        
        self.subject = subject
        
        self.body = body
        
        self.priority = "Normal"
    
    def send(self,email_manager):
        
        email_manager.send(self)
        
