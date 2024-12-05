from HouseBuilder import HouseBuilder
def main():
    
    builder = HouseBuilder()
    
    my_house = (builder
                .add_floors(2)
                .add_rooms(4)
                .add_garage()
                .add_pool()
                .build())
    
    print(my_house)  # Output: House with 2 floor(s), 4 room(s), a garage, a pool, no garden.

if __name__ == "__main__":
    main()
