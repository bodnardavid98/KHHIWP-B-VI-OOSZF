from Auto import Auto

class PersonalVehicle(Auto):
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