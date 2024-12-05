from House import House
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def add_floors(self, floors):
        self.house.floors = floors
        return self

    def add_rooms(self, rooms):
        self.house.rooms = rooms
        return self

    def add_garage(self):
        self.house.garage = True
        return self

    def add_pool(self):
        self.house.pool = True
        return self

    def add_garden(self):
        self.house.garden = True
        return self

    def build(self):
        return self.house
