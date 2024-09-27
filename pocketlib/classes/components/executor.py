from abc import ABC, abstractmethod
from pocketlib.classes.abc.component import Component
from pocketlib.classes.abc.conduit import Conduit
from pocketlib.classes.data.results import ExecutionResult

class Executor(Component, Conduit):
    @abstractmethod
    def execute_cmd(self, cmd: str) -> ExecutionResult:
        """
        This method receives a commandline and executes it, returning the status of the execution.
        No command output will be returned from this method - this is the retriever's job ;)
        """
