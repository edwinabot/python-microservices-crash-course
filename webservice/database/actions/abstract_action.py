from abc import ABC, abstractmethod

class DatabaseAction(ABC):

    @abstractmethod
    def create_statement(self):
        raise NotImplementedError
