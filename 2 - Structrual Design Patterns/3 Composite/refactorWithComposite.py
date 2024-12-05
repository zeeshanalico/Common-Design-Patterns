from abc import ABC, abstractmethod

# Define the common Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent=""):
        pass

# Implement the File class
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def display(self, indent=""):
        print(f"{indent}- {self.name} ({self.size} KB)")

# Implement the Folder class
class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.contents = []

    def add(self, component: FileSystemComponent):
        self.contents.append(component)

    def get_size(self) -> int:
        return sum(item.get_size() for item in self.contents)

    def display(self, indent=""):
        print(f"{indent}+ {self.name}/")
        for item in self.contents:
            item.display(indent + "  ")

# Creating a sample file structure
root_folder = Folder("root")
root_folder.add(File("file1.txt", 10))
root_folder.add(File("file2.txt", 20))

sub_folder = Folder("sub_folder")
sub_folder.add(File("file3.txt", 15))
root_folder.add(sub_folder)

# Display structure and sizes
root_folder.display()
print("Total size:", root_folder.get_size(), "KB")
