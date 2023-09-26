from abc import ABC,abstractmethod

class SenderMail(ABC):
    
    @abstractmethod
    def send(self):
        pass