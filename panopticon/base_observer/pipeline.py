from abc import ABC

from panopticon.base_observer.observing import BaseObserver
from panopticon.base_observer.response import ObserverResponse

class Pipeline(BaseObserver, ABC):
    def __init__(self, observers: tuple | dict | list):
        self.observers = observers


    def check(self) -> dict:
        ret = {}

        if isinstance(self.observers, dict):
            for name, observer in self.observers.items():
                ret[name] = observer.check()
                if isinstance(ret[name], ObserverResponse):
                    ret[name] = ret[name].to_dict()
        else:
            for observer in self.observers:
                if isinstance(observer, tuple) or isinstance(observer, list):
                    if len (observer) != 2:
                        raise ValueError("Invalid observer tuple")
                    ret[observer[0]] = observer[1].check()
                    name = observer[0]
                else:
                    ret[type(observer).__name__] = observer.check()
                    name = type(observer).__name__
                if isinstance(ret[name], ObserverResponse):
                    ret[name] = ret[name].to_dict()

        return ret


