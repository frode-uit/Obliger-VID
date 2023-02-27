# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():
    # Create empty list for vehicles
    vehicles_list = []
    # Create a Car object for a used 2001 BMW
    # with 70,000 miles, priced at $15,000, with
    # 4 doors.
    car = vehicles.Car('BMW 320', 2001, 70000, 15000.0, 4)
    vehicles_list.append(car)
    # Create a Truck object for a used 2002
    # Toyota pickup with 40,000 miles, priced
    # at $12,000, with 4-wheel drive.
    truck = vehicles.Truck('Toyota RAV4', 2002, 40000, 12000.0, '4WD')
    vehicles_list.append(truck)
    # Create an SUV object for a used 2000
    # Volvo with 30,000 miles, priced
    # at $18,500, with 5 passenger capacity.
    suv = vehicles.SUV('Volvo XC60', 2010, 30000, 18500.0, 5)
    vehicles_list.append(suv)

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('Add a new car')
        elif choice == NEW_TRUCK_CHOICE:
            print('Add a new truck')
        elif choice == NEW_SUV_CHOICE:
            print('Add a new SUV')
        elif choice == FIND_VEHICLE_CHOICE:
            print('Find vehicle by name')
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')    
        else:
            print('Error: invalid selection.')    

# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')     

# Call the main function.
if __name__ == '__main__':
      main()