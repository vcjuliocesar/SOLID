from abc import ABC,abstractmethod

class ManagerPriority(ABC):
    
    @abstractmethod
    def set_priority(self):
        pass