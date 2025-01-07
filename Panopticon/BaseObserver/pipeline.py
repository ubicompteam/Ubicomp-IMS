from abc import ABC

from Panopticon.BaseObserver.observing import BaseObserver

class Pipeline(BaseObserver, ABC):
    def __init__(self, observers: tuple | dict):
        self.observers = observers


    def check(self):
        ret = {}
        try:
            if isinstance(self.observers, dict):
                for name, observer in self.observers.items():
                    ret[name] = observer.check()
            else:
                for observer in self.observers:
                    if isinstance(observer, tuple):
                        ret[observer[0]] = observer[1].check()
                    else:
                        ret[type(observer).__name__] = observer.check()
        except Exception as e:
            return str(e)

        return ret


