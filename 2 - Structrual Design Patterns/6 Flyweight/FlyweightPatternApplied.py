class TreeType:
    """Flyweight class that stores shared (intrinsic) data for trees."""
    _instances = {}

    def __new__(cls, name, color, texture, height):
        key = (name, color, texture, height)
        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)
        return cls._instances[key]

    def __init__(self, name, color, texture, height):
        self.name = name
        self.color = color
        self.texture = texture
        self.height = height

class Tree:
    """Class that stores unique (extrinsic) data for trees."""
    def __init__(self, tree_type, location_x, location_y):
        self.tree_type = tree_type
        self.location_x = location_x
        self.location_y = location_y

    def display(self):
        print(f"Tree: {self.tree_type.name}, Color: {self.tree_type.color}, "
              f"Height: {self.tree_type.height}, Location: ({self.location_x}, {self.location_y})")

# Example usage of Flyweight pattern
forest = [
    Tree(TreeType("Oak", "Green", "Rough", 20), 5, 10),
    Tree(TreeType("Pine", "Dark Green", "Smooth", 30), 15, 30),
    Tree(TreeType("Oak", "Green", "Rough", 20), 50, 60),
    Tree(TreeType("Pine", "Dark Green", "Smooth", 30), 25, 80),
]

for tree in forest:
    tree.display()
