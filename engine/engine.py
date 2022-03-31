from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        '''Method to check for when service is needed'''