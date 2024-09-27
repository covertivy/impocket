from abc import ABC, abstractmethod


class Conduit(ABC):
    @abstractmethod
    def preconnect(self):
        pass
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def postconnect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def reconnect(self):
        pass
