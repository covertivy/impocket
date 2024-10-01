from abc import ABC, abstractmethod
from pocketlib.classes.abc.component import Component
from pocketlib.classes.abc.conduit import Conduit
from pocketlib.classes.data.results import RetrievalResult

class Retriever(Component, Conduit):
    @abstractmethod
    def retrieve_data(self) -> RetrievalResult:
        """
        This method retrieves output of a command, returning the status of the retrieval and the raw data.
        """
