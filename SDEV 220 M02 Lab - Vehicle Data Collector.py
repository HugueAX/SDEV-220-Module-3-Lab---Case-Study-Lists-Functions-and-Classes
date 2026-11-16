# Raven Chason
# SDEV 220 M02 Lab - Vehicle Data Collector
# This application will

# defines a super class called Vehicle
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# defines a chiled class called Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# asks user for Vehicle type and 
# stores into the vehicle_type in Vehicle class
vehicle_type = input("\nPlease enter your vehicle type (car, truck, plane, boat, or broomstick): ").strip().lower()

while vehicle_type != "car":  #only doing cars
    print("\nSorry, only accepting cars at this time.")
    vehicle_type = input("\nPlease enter your vehicle type (car, truck, plane, boat, or broomstick): ")

if vehicle_type == "car":
    year = input("\nPlease enter the year of manufacture: ")
    make = input("\nPlease enter the make: ")
    model = input("\nPlease enter the model: ")
    while True:
        doors = input("\nPlease enter the number of doors (2 or 4): ")
        if doors == "2" or doors == "4":
            break
        print("\nSorry, invalid response. Please enter 2 or 4.")
    
    while True: 
        roof = input("\nPlease enter the type of roof (Solid or Sun): ").strip().capitalize()
        if roof == "Sun" or roof == "Solid":
            break
        print(f"\nSorry, invalid response. Please enter Solid or Sun.")

# creates an instance of Automobile to store the data
car1 = Automobile(vehicle_type, year, make, model, doors, roof)

#output data
print("\n***** Vehicle Data *****\n")
print(f"Vehicle Type: {car1.vehicle_type}")
print(f"Year: {car1.year}")
print(f"Make: {car1.make}")
print(f"Model: {car1.model}")
print(f"Number of Doors: {car1.doors}")
print(f"Type of Roof: {car1.roof}")
print("\nThank you for your time.\n")