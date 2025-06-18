from abc import ABC, abstractmethod
class Example(ABC):
    @abstractmethod
    def abstract_method(self):
        raise NotImplementedError
    def concrete_method(self):
        return True
