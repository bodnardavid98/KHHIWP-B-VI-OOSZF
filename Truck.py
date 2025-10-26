from Auto import Auto

class Truck(Auto):
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