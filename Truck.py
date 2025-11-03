from Auto import Auto

class Truck(Auto):
    # Final class inherited from Auto for single truck

    # Amount of cargo space, in m^2
    __cargoSpace = 15

    def __init__(self, license, pricePerDay, cargoSpace):
        Auto.__init__(self, license, "Truck", pricePerDay)
        self.__cargoSpace = cargoSpace

    @property
    def CargoSpace(self):
        return self.__cargoSpace

    @CargoSpace.setter
    def CargoSpace(self, cargoSpace):
        self.__cargoSpace = cargoSpace

    def __str__(self):
        # Function to convert class object to string, writes license, type, cargo capacity and rent price per day

        return "%s rendszámú tehergépjármű, %d köbméter tárolóhellyel, %d kölcsönzési díjjal" % (self.License, self.__cargoSpace, self.PricePerDay)
