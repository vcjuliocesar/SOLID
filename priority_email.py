from email_address import EmailAddress
 
class PriorityEmail(EmailAddress):
    
    def __init__(self) -> None:
        
        super().__init__()
        
        self.priority = "Normal"
        
    def set_priority(self,priority:str):
        
        self.priority = priority
    
    def send(self):
        
        print(f"Email sent from {self.sender} to {self.addressee} with subject {self.subject}, priority: {self.priority}")
