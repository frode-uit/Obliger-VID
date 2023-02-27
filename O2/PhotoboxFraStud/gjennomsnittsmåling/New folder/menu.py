# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles
import radars
import pickle

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 7
CHECK_SPEEDING_TICKETS = 6

def main():
    # Create empty list for vehicles
    vehicles_list = []
    dictionary = {}

    try:
        dictionary = radars.listSpeeders('box_a.txt', 'box_b.txt', 60, 5)
    except:
        print("Failed to generate dictionary. No speeding tickets are registered.\n")

    try:
        with open('vehicles.pkl', 'rb') as fil:
            vehicles_list = pickle.load(fil)
    except:
        print("Failed to open vehicles.pkl. Starting program with an empty list.\n")
    
    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
            print()
        except:
            print("\nPlease use an integer value between 1 and 7.")

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('Input car data:')
            make, model, mileage, price, registration = grab_shared_data()
            doors = int(input('Doors: '))
            vehicles_list.append(vehicles.Car(make, model, mileage, price, registration, doors))
        elif choice == NEW_TRUCK_CHOICE:
            print('Input truck data:')
            make, model, mileage, price, registration = grab_shared_data()
            drive_type = input('Drive type: ')
            vehicles_list.append(vehicles.Truck(make, model, mileage, price, registration, drive_type))
        elif choice == NEW_SUV_CHOICE:
            print('Input SUV data:')
            make, model, mileage, price, registration = grab_shared_data()
            pass_cap = int(input('Number of passengers: '))
            vehicles_list.append(vehicles.SUV(make, model, mileage, price, registration, pass_cap))
        elif choice == FIND_VEHICLE_CHOICE:
            make = input('Name of vehicle: ')
            for item in vehicles_list:
                if make in item.get_make():
                    print(item)
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)
        elif choice == CHECK_SPEEDING_TICKETS:
            print('Found the following violations:')
            for vehicle in vehicles_list:
                try:
                    if dictionary[vehicle.get_registration()]:
                        ticket = radars.SpeedTicket(vehicle.get_registration(), dictionary[vehicle.get_registration()][1], dictionary[vehicle.get_registration()][0], 60)
                        exists = False
                        for violation in vehicle.get_violations():
                            if violation.check_time(dictionary[vehicle.get_registration()][1]):
                                exists = True
                        if not exists: 
                            vehicle.add_violation(ticket)
                except KeyError:
                    pass
                for violation in vehicle.get_violations():
                    print(str(vehicle.get_model()) + " " + vehicle.get_make() + " with registration number " + str(violation))
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')    
            vehicles_list = sorted(vehicles_list, key=lambda x: x.get_make().lower())
            try:
                with open('vehicles.pkl', 'wb') as fil:
                    pickle.dump(vehicles_list, fil)
            except:
                print("Failed to write to vehicles.pkl. No data will be saved.")
        else:
            print('Error: invalid selection.')    
        print()

# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Check speeding tickets')
    print('7) Quit')     

def grab_shared_data():
    make = input('Make: ')
    model = int(input('Model: '))
    mileage = int(input('Mileage: '))
    price = float(input('Price: '))
    registration = input('Registration: ')
    return make, model, mileage, price, registration

# Call the main function.
if __name__ == '__main__':
      main()