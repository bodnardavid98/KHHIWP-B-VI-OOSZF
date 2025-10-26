from Auto import Auto

class Rental:
    # Final class for a single rent of a single auto

    # The auto being rented
    __auto = Auto(None, None, None)

    # Start of renting period
    __start = []

    # End of renting period
    __end = []

    def __init__(self, auto, start, end):
        self.__auto = auto
        self.__start = start
        self.__end = end
