from abc import ABC, abstractmethod
from pocketlib.classes.abc.component import Component
from pocketlib.classes.abc.conduit import Conduit
from pocketlib.classes.data.results import UtilityResult

class Utility(Component, Conduit):
    @abstractmethod
    def run_logic(self, env: dict) -> UtilityResult:
        """
        This command runs a utility's logic, returning the result of the logic execution.
        """
