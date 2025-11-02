from PersonalVehicle import PersonalVehicle
from Truck import Truck
from Rental import Rental

auto = PersonalVehicle("asd-123", 20000, 2)
auto = Truck("asd-123", 20000, 20)
print(auto.Type)

rental = Rental("Car rental company")

while True:
    print("Válaszd ki a funkciót.\n 1 Autó bérlése\n 2 Bérlés lemondása\n 3 Bérlések listázása\n 4 Kilépés")
    Function = input()
    if Function != "1" and Function != "2" and Function != "3" and Function != "4":
        print("Ez nem egy opció")
    else:
        if Function == "3":
            rental.printRents()
        if Function == "4":
            break