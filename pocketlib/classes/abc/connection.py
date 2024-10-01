from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def reconnect(self):
        pass
