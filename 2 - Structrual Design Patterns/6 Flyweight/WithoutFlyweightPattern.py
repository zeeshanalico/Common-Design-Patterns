class Tree:
    def __init__(self, name, color, texture, height, location_x, location_y):
        self.name = name
        self.color = color
        self.texture = texture
        self.height = height
        self.location_x = location_x
        self.location_y = location_y

    def display(self):
        print(f"Tree: {self.name}, Color: {self.color}, Height: {self.height}, "
              f"Location: ({self.location_x}, {self.location_y})")

# Example usage
forest = [
    Tree("Oak", "Green", "Rough", 20, 5, 10),
    Tree("Pine", "Dark Green", "Smooth", 30, 15, 30),
    Tree("Oak", "Green", "Rough", 20, 50, 60),
    Tree("Pine", "Dark Green", "Smooth", 30, 25, 80),
]

for tree in forest:
    tree.display()
