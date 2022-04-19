from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def greet(self):
        print('Hola, soy un ' + self.get_type())