from PersonalVehicle import PersonalVehicle
from Truck import Truck
from Rental import Rental

rental = Rental("Car rental company")
rental.addCar(Truck("ASD-123", 20000, 20))
rental.addCar(PersonalVehicle("QWE-456", 10000, 2))
rental.addCar(PersonalVehicle("YXC-789", 15000, 4))

while True:
    print("Válaszd ki a funkciót.\n 1 Autó bérlése\n 2 Bérlés lemondása\n 3 Bérlések listázása\n 4 Kilépés")
    Function = input()
    if Function != "1" and Function != "2" and Function != "3" and Function != "4":
        print("Ez nem egy opció")
    else:
        if Function == "1":
            rental.bookRent()
        elif Function == "2":
            rental.backRent()
        elif Function == "3":
            rental.printRents()
        elif Function == "4":
            break