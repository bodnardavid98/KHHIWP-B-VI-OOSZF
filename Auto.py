class Auto:
    # Abstract class for a single car

    # License plate
    __license = ""

    # Car type, used by final classes
    __type = ""

    # Price to loan car for a day, in HUF
    __pricePerDay = 10000

    def __init__(self, license, type, pricePerDay):
        self.__license = license
        self.__type = type
        self.__pricePerDay = pricePerDay

    @property
    def License(self):
        return self.__license

    @License.setter
    def License(self, license):
        self.__license = license

    @property
    def Type(self):
        return self.__type

    @Type.setter
    def Type(self, type):
        self.__type = type

    @property
    def PricePerDay(self):
        return self.__pricePerDay

    @PricePerDay.setter
    def PricePerDay(self, pricePerDay):
        self.__pricePerDay = pricePerDay


