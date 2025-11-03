from Auto import Auto

class Rent:
    # Final class for a single rent of a single auto

    # The auto being rented
    __auto = Auto(None, None, None)

    # Start of renting period
    __start = ""

    # End of renting period
    __end = ""

     # Number of days the rent lasts
    __days = 0

    def __init__(self, auto, start, end, days):
        self.__auto = auto
        self.__start = start
        self.__end = end
        self.__days = days

    @property
    def Auto(self):
        return self.__auto

    @property
    def Start(self):
        return self.__start

    @property
    def End(self):
        return self.__end

    def __str__(self):
        # Function to convert class object to string, writes license, start and end dates and full price of rent

        return "%s kölcsönözve %s-től %s-ig, ára: %d" % (self.__auto.License, self.Start, self.End, self.__days * self.__auto.PricePerDay)



