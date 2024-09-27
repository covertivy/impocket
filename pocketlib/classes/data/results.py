from abc import ABC
from dataclasses import dataclass
from enum import StrEnum, auto


class ComponentActionStatus(StrEnum):
    success = auto("Success")
    error = auto("Error")
    cancelled = auto("Cancelled")


@dataclass
class ComponentResult(ABC):
    # The status of the executor's action.
    status: ComponentActionStatus
    
    # The error that had occured during the execution (if any occured).
    # If the status of the execution returned "Error" - this value should be checked.
    err: Exception = None           

    # Should we terminate the executor's connection after this action?
    terminate: bool


@dataclass
class ExecutionResult(ComponentResult):
    pass


@dataclass
class UtilityResult(ComponentResult):
    pass


@dataclass
class RetrievalResult(ComponentResult):
    # The raw data returned by the retriever's action.
    raw: bytes
