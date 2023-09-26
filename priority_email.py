from email_address import EmailAddress
from priority_manager import PriorityManager
 
class PriorityEmail(PriorityManager):
    
    # def __init__(self) -> None:
        
    #     super().__init__()
        
    #     self.priority = "Normal"
        
    def set_priority(self,email,priority:str):
        
        email.priority = priority
    
    # def send(self):
        
    #     print(f"Email sent from {self.sender} to {self.addressee} with subject {self.subject}, priority: {self.priority}")
