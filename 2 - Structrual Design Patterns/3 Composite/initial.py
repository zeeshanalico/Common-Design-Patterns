class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def display(self, indent=""):
        print(f"{indent}- {self.name} ({self.size} KB)")

class Folder:
    def __init__(self, name: str):
        self.name = name
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def get_size(self) -> int:
        total_size = 0
        for item in self.contents:
            if isinstance(item, File):
                total_size += item.get_size()
            elif isinstance(item, Folder):
                total_size += item.get_size()
        return total_size

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


# + root/
#   - file1.txt (10 KB)
#   - file2.txt (20 KB)
#   + sub_folder/
#     - file3.txt (15 KB)
# Total size: 45 KB
