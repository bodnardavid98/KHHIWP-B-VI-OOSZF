import re, datetime
from Rent import Rent

class Rental:
    # Final class for a company providing cars for rent

    # Name of company
    __name = ""

    # List of all cars the company owns
    __cars = []

    # List of all ongoing and past rents
    __rents = []

    __dateRegex = re.compile("(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)")

    def __init__(self, name):
        self.__name = name

    def getDate(self, name, car):
        date = "-2"
        while True:
            date = input("Adj meg egy %s dátumot (yyyy-mm-dd), vagy -1 visszalépéshez: " % name)
            if date == "-1":
                return date
            else:
                dateResult = self.__dateRegex.match(date)
                if dateResult == None:
                    print("Rossz dátum formátum")
                else:
                    year, month, day = dateResult.group(1), dateResult.group(2), dateResult.group(3)
                    try:
                        datetime.date(int(year), int(month), int(day))

                        found = False
                        for rent in self.__rents:
                            if car == rent.Auto and rent.Start <= date and date <= rent.End:
                                print("Ez az autó ekkor már foglalt")
                                found = True
                                break
                        if not found:
                            return date
                    except:
                        print("Ilyen dátum nem létezik")

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

        start, end = "-2", "-2"
        while True:
            start = self.getDate("kezdő", self.__cars[car])
            if start == "-1":
                return
            end = self.getDate("befejező", self.__cars[car])
            if end == "-1":
                return

            if end < start:
                print("A befejező dátum nem lehet korábban a kezdő dátumnál")
            else:
                break

        startResult = self.__dateRegex.match(start)
        endResult = self.__dateRegex.match(end)
        startyear, startmonth, startday = startResult.group(1), startResult.group(2), startResult.group(3)
        endyear, endmonth, endday = endResult.group(1), endResult.group(2), endResult.group(3)
        startDate = datetime.date(int(startyear), int(startmonth), int(startday))
        endDate = datetime.date(int(endyear), int(endmonth), int(endday))
        datedifference = endDate - startDate

        self.__rents.append(Rent(self.__cars[car], start, end, datedifference.days + 1))
        print("Bérlés felvéve: %s" % str(self.__rents[-1]))

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