from abc import ABC, abstractmethod

from base_observer.response import ObserverResponse


class BaseObserver(ABC):
    @abstractmethod
    def check(self) -> ObserverResponse:
        pass
