from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        return "Render a button in Windows style"

class MacOSButton(Button):
    def paint(self):
        return "Render a button in macOS style"

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in Windows style"

class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in macOS style"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()
    def create_checkbox(self):
        return MacOSCheckbox()



# Client code
def client(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

# Usage
if __name__ == "__main__":
    os_choice = "Windows"  # Change to "macOS" for macOS elements
    factory = WindowsFactory() if os_choice == "Windows" else MacOSFactory()
    client(factory)
