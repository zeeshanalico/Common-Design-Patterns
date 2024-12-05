from subsystems import FlightBooking, HotelBooking, CarRental

class TravelFacade:
    def __init__(self):
        self.flight_booking = FlightBooking()
        self.hotel_booking = HotelBooking()
        self.car_rental = CarRental()

    def book_vacation(self, destination: str):
        print("Booking your vacation package...")
        flight = self.flight_booking.book_flight(destination)
        hotel = self.hotel_booking.book_hotel(destination)
        car = self.car_rental.book_car(destination)
        print(flight)
        print(hotel)
        print(car)
        print("Vacation package booked successfully!")



if __name__ == "__main__":
    destination = "Paris"
    
    travel_facade = TravelFacade()
    travel_facade.book_vacation(destination)