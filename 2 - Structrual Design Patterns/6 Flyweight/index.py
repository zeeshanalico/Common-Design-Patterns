from typing import Dict

# Flyweight class
class CharacterStyle:
    """Flyweight class to store character styles."""
    def __init__(self, font: str, size: int, color: str):
        self.font = font
        self.size = size
        self.color = color

    def __str__(self):
        return f"Style({self.font}, {self.size}px, {self.color})"

# Flyweight Factory
class CharacterStyleFactory:
    """Factory to manage the flyweight objects."""
    _styles: Dict[str, CharacterStyle] = {}

    @classmethod
    def get_style(cls, font: str, size: int, color: str) -> CharacterStyle:
        """Return a shared CharacterStyle object."""
        key = f"{font}-{size}-{color}"
        if key not in cls._styles:
            cls._styles[key] = CharacterStyle(font, size, color)
            print(f"Creating new style: {cls._styles[key]}")
        else:
            print(f"Reusing existing style: {cls._styles[key]}")
        return cls._styles[key]

# Context class that uses the Flyweight
class Character:
    """Represents a character with a position and shared style."""
    def __init__(self, char: str, style: CharacterStyle, x: int, y: int):
        self.char = char
        self.style = style
        self.x = x
        self.y = y

    def display(self):
        print(f"Character '{self.char}' at ({self.x}, {self.y}) with style {self.style}")

# Client code
if __name__ == "__main__":
    # Using the Flyweight Factory to create/reuse styles
    style1 = CharacterStyleFactory.get_style("Arial", 12, "black")
    style2 = CharacterStyleFactory.get_style("Arial", 12, "black")
    style3 = CharacterStyleFactory.get_style("Times New Roman", 14, "blue")

    # Creating characters with shared styles
    char1 = Character("H", style1, 10, 10)
    char2 = Character("e", style1, 20, 10)
    char3 = Character("l", style2, 30, 10)
    char4 = Character("o", style3, 40, 10)

    # Displaying characters
    char1.display()
    char2.display()
    char3.display()
    char4.display()
