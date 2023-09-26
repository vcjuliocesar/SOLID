from abc import ABC,abstractmethod

class PriorityManager(ABC):
    
    @abstractmethod
    def set_priority(self):
        pass