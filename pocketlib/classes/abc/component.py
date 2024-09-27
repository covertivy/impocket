from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def load(self, env):
        pass

    @abstractmethod
    def unload(self):
        pass
