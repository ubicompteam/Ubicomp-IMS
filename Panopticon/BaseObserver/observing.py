from abc import ABC, abstractmethod
from Panopticon.BaseObserver.response import ObserverResponse

class BaseObserver(ABC):
    @abstractmethod
    def check(self) -> ObserverResponse:
        pass
