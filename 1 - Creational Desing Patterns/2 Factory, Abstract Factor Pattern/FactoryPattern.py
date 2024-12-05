from abc import ABC, abstractmethod

# Step 1: Create an interface or abstract class for products
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class Hilton(Product):
    def operation(self):
        return "Result from Hilton"

class Dior(Product):
    def operation(self):
        return "Result from Dior"

class Factory(ABC):#abstract Creator
    @abstractmethod
    def factory_method(self):   
        pass

class HiltonFactory(Factory):#concrete Creator
    def factory_method(self):
        return Hilton()

class DiorFactory(Factory):#concrete Creator
    def factory_method(self):
        return Dior()

def client_code(factory: Factory):
    product = factory.factory_method()
    print(product.operation())

# Usage
client_code(HiltonFactory())  
client_code(DiorFactory())     
