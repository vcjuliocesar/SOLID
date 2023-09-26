from abc import ABC,abstractmethod

class EmailManager(ABC):
    
    @abstractmethod
    def send(self):
        pass
    
