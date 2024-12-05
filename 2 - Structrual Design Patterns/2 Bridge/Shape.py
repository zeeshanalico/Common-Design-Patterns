from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass

class Red(Color):
    def paint(self) -> str:
        return "Red"

class Blue(Color):
    def paint(self) -> str:
        return "Blue"

# Abstraction
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self) -> None:
        pass

class Circle(Shape):
    def draw(self) -> None:
        print(f"Drawing a {self.color.paint()} Circle")

class Square(Shape):
    def draw(self) -> None:
        print(f"Drawing a {self.color.paint()} Square")

# Client code
if __name__ == "__main__":
    red_color = Red()
    blue_color = Blue()

    red_circle = Circle(red_color)
    blue_circle = Circle(blue_color)

    red_square = Square(red_color)
    blue_square = Square(blue_color)

    # Drawing shapes
    red_circle.draw()   # Output: Drawing a Red Circle
    blue_circle.draw()  # Output: Drawing a Blue Circle
    red_square.draw()   # Output: Drawing a Red Square
    blue_square.draw()  # Output: Drawing a Blue Square
