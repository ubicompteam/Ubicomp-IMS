from abc import ABC, abstractmethod
from panopticon.base_observer.response import ObserverResponse

class BaseObserver(ABC):
    @abstractmethod
    def check(self) -> ObserverResponse:
        pass
