class Auto:
    _license = ""
    _type = ""
    _pricePerDay = 1000

    def __init__(self, license, type, pricePerDay):
        self._license = license
        self._type = type
        self._pricePerDay = pricePerDay

    @property
    def License(self):
        return self._license

    @License.setter
    def License(self, license):
        self._license = license

    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self, type):
        self._type = type

    @property
    def PricePerDay(self):
        return self._pricePerDay

    @PricePerDay.setter
    def PricePerDay(self, pricePerDay):
        self._pricePerDay = pricePerDay


