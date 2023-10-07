from abc import ABC,abstractmethod

class car(ABC):

    @abstractmethod
    def start(self):
        pass
        
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

class swift(car):

    def start(self):
        print("swift starts")

    def stop(self):
        print("swift stops")

    def accelerate(self):
        print("swift accelerate")


obj=swift()
obj.accelerate()
