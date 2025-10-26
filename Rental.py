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
            print("There is no such rent.")

    def printRents(self):
        for rent in self.__rents:
            print(rent.Car().License() + " rented from " + rent.Start() + " to " + rent.End())
