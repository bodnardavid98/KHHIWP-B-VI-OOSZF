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
