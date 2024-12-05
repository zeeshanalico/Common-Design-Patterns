from abc import ABC, abstractmethod
#Circle and Rectangle are Leaf components
# Group is a Composite component.
class Graphic(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Circle(Graphic):
    def render(self) -> str:
        return "Circle"

class Rectangle(Graphic):
    def render(self) -> str:
        return "Rectangle"


class Group(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic: Graphic):
        self.children.append(graphic)

    def remove(self, graphic: Graphic):
        self.children.remove(graphic)

    def render(self) -> str:
        results = []
        for child in self.children:
            results.append(child.render())
        return "Group(" + ", ".join(results) + ")"



if __name__=='__main__':
    # Create simple objects
    circle = Circle()
    rectangle = Rectangle()
    
    group1 = Group()
    group1.add(circle)
    group1.add(rectangle)
    
    group2 = Group()
    group2.add(group1)
    group2.add(Rectangle())
    
    # Render everything
    print(group2.render())

