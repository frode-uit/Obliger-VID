#Car, Truck and SUV Demo 
import vehicles
import os
import pickle

NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():

    try:
        savefile = "Oblig1/list_of_vehicles.dat"
        
        if os.path.isfile(savefile):
            dat_of_vehicles = open(savefile, "rb")
            vehicles_list = pickle.load(dat_of_vehicles)
            dat_of_vehicles.close()
        else:
            vehicles_list = []
            
        choice = 0
        while choice != QUIT_CHOICE:
            display_menu()
            choice = int(input('Enter your choice: '))

            if choice == NEW_CAR_CHOICE:
                print("\nAdd  a new car")

                new_car = vehicles.Car(
                    input("Please enter make and model of car: "),
                    int(input("Please enter year of the make: ")),
                    int(input("Please enter milage of the car: ")),
                    float(input("Please enter the price of the new car: ")),
                    int(input("Please enter number of doors: ")))
                vehicles_list.append(new_car)

            elif choice == NEW_TRUCK_CHOICE:
                print("\nAdd a new truck")

                new_car = vehicles.Truck(
                    input("Please enter make and model of car: "),
                    int(input("Please enter year of the make: ")),
                    int(input("Please enter milage of the car: ")),
                    float(input("Please enter the price of the new car: ")),
                    input("Please enter drivetype(front/rear-wheel or 4WD): "))
                vehicles_list.append(new_car)

            elif choice == NEW_SUV_CHOICE:
                print("\nAdd a new SUV")

                new_car = vehicles.SUV(
                    input("Please enter make and model of car: "),
                    int(input("Please enter year of the make: ")),
                    int(input("Please enter milage of the car: ")),
                    float(input("Please enter the price of the new car: ")),
                    int(input("Please enter maximum number of passengers: ")))
                vehicles_list.append(new_car)

            elif choice == FIND_VEHICLE_CHOICE:
                make = input("\nName of vehicle: \n")

                for item in vehicles_list:
                    if make in item.__str__():
                        print(item)
                    
            elif choice == SHOW_VEHICLES_CHOICE:
                print('\nThe following cars are in inventory:')
                
                for item in vehicles_list:
                    print(item.__str__())

            elif choice == QUIT_CHOICE:
                print('Exiting the program...') 

                sorted_vehicle_list = sorted(vehicles_list, key = lambda cars: cars.__str__())
                
                try:
                    dat_of_vehicles = open(savefile, "wb")
                    pickle.dump(sorted_vehicle_list, dat_of_vehicles)
                    dat_of_vehicles.close()
                    
                except FileNotFoundError:
                    print(f'\nDirectory not found. Save was not complete.')
            
            else:
                print('Error: invalid selection.\n')

    except ValueError as ex:
        print(f'\nException: {ex}. Try again.')
        main()

def display_menu():
    print('\n        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')     

if __name__ == '__main__':
    main()