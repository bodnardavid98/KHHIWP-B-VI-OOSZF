from Auto import Auto

class PersonalVehicle(Auto):
    # Final class inherited from Auto for single personal vehicle

    # Number of passenger/driver seats
    __seats = 4

    def __init__(self, license, pricePerDay, seats):
        Auto.__init__(self, license, "PersonalVehicle", pricePerDay)
        self.__seats = seats

    @property
    def Seats(self):
        return self.__seats

    @Seats.setter
    def Seats(self, seats):
        self.__seats = seats

    def __str__(self):
        return "%s rendszámú személyautó, %d üléssel, %d kölcsönzési díjjal" % (self.License, self.__seats, self.PricePerDay)
