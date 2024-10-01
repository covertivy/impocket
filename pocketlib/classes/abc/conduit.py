from abc import ABC, abstractmethod
from pocketlib.classes.abc.connection import Connection


class Conduit(ABC, Connection):
    @abstractmethod
    def preconnect(self):
        pass
    
    @abstractmethod
    def postconnect(self):
        pass
