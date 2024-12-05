from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Vehicle(Prototype):
    def __init__(self, model, engine, color): 
        self.model = model
        self.engine = engine
        self.color = color

    def __str__(self):  
        
        return f"Car(Model: {self.model}, Engine: {self.engine}, Color: {self.color}, ToSpeed: {self.toSpeed})"

    def __repr__(self):  
        return f"Car(Model={self.model}, Engine={self.engine}, Color={self.color}, ToSpeed={self.toSpeed})"

    def clone(self):
        return copy.deepcopy(self)

    
class Car(Vehicle):
    def __init__(self, model, engine, color, toSpeed):
        
        super().__init__(model, engine, color) 
        self.toSpeed = toSpeed
    def clone(self):
        return Car(model=self.model, engine=self.engine, color=self.color, toSpeed=self.toSpeed)

        
class Bus(Vehicle):
    def __init__(self, model, engine, color, wheels):
        super().__init__(model, engine, color) 
        self.wheels = wheels
    
    def clone(self):
        return Bus(model=self.model, engine=self.engine, color=self.color, wheels=self.wheels)




        
if __name__ == "__main__":
    car = Car(model="Sedan", engine="V6", color="Reda", toSpeed=150)
    cloned_car = car.clone()  # Clone the Car object
    cloned_car.model = "New Model"  # Change the model of the cloned object
    print(f"Original Car : {car}") # print(f"Original Car : {str(car)}")  # both are same and will call __str__
    print(f"Cloned Car : {repr(cloned_car)}")  # Print cloned model
