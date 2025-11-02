class Rental:
    # Final class for a company providing cars for rent

    # Name of company
    __name = ""

    # List of all cars the company owns
    __cars = []

    # List of all ongoing and past rents
    __rents = []

    def __init__(self, name):
        self.__name = name

    def bookRent(self):
        for car in self.__cars:
            print(str(self.__cars.index(car)) + " " + str(car))

        car = "-2"
        while True:
            car = input("Válassz egy autót kölcsönzésre, vagy -1 visszalépéshez: ")
            if car == "-1":
                return
            else:
                try:
                    carNumber = int(car)
                    if -1 < carNumber and carNumber < len(self.__cars):
                        car = carNumber
                        break
                    else:
                        print("Nincs ilyen indexű autó")
                except:
                    print("Ez nem egy szám")

    def backRent(self):
        print(str(self) + "Válassz egy kölcsönzést a lemondásra")

    def addCar(self, car):
        self.__cars.append(car)

    def deleteRent(self, rentID):
        if self.__rents.Length() > rentID:
            del self.__rents[rentID]
        else:
            print("Nincs ilyen bérlés.")

    def printRents(self):
        print(self)

    def __str__(self):
        result = "Az %s cég összes elmentett bérlése (%d darab):\n" % (self.__name, len(self.__rents))
        for rent in self.__rents:
            result += str(rent) + "\n"
        return result