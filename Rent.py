from Auto import Auto

class Rent:
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
        return "%s kölcsönözve %s-től %s-ig" % (self.__auto.License, self.Start, self.End)



