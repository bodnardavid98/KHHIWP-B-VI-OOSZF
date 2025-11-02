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