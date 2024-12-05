class House:
    def __init__(self):
        self.floors = 0
        self.rooms = 0
        self.garage = False
        self.pool = False
        self.garden = False

    def __str__(self):
        return (f"House with {self.floors} floor(s), "
                f"{self.rooms} room(s), "
                f"{'a garage' if self.garage else 'no garage'}, "
                f"{'a pool' if self.pool else 'no pool'}, "
                f"{'a garden' if self.garden else 'no garden'}.")
