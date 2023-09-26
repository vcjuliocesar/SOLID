from interfaces.priority_manager import PriorityManager
 
class PriorityEmail(PriorityManager):
        
    def set_priority(self,email,priority:str):
        
        email.priority = priority

