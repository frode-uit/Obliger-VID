'''Written by Jøran Lillegård'''
import sys
import pickle
import globals
import speedTickets
import generate_car_list
from os import system
from functools import partial
from vehicles import add_vehicle

# The display_menu function displays a menu.
def displayMenu(menu):
    '''Function to show all the menu options'''
    print('\n')
    for i in menu:
        for x in menu[i]:
            print(i, menu[i][x])        
    choice = input('Please enter your menu number >>> ')
    return choice
    
def main():
    # Dictionary with all the menu options
    menu_choices = {1: {partial(newVehicle, globals.NEW_CAR_CHOICE): 'New car'}, 2: {partial(newVehicle, globals.NEW_TRUCK_CHOICE): 'New Truck'}, 
                    3: {partial(newVehicle, globals.NEW_SUV_CHOICE): 'New SUV'}, 4: {searchVehicle: 'Find vehicles by make'}, 
                    5: {showAllVehicle: 'Show all vehicles'}, 6: {showVehicleTickets: 'Update/Show all vehicles with tickets'},
                    7: {quit: 'Quit'}}
    vehicles_list = []
    
    try:
        with open(globals.VEHICLE_DB, 'rb') as fp:
            print('\nLoading database\n')
            vehicles_list = pickle.load(fp)
    except EOFError:
        # If program suddenly exits and the database is empty, it will ganerate a new vehicle list
        vehicles_list = generate_car_list.generateCars()
    except FileNotFoundError:
        # If the database is not found it will generate a new empty file
        print('\nNo database found, creating file\n')
        with open(globals.VEHICLE_DB, 'w') as fp:
            pass
        vehicles_list = generate_car_list.generateCars()     
       
    while True:
        choice = displayMenu(menu_choices)
        try:
            for menu_choice in menu_choices[int(choice)]:
                menu_choice(vehicles_list)
        except KeyError:
            print('\n***Invalid menu choice***')
        except ValueError:
            print('\n***Invalid menu choice***')

def newVehicle(vehicle_type, vehicles_list):
    '''Menu option for adding a new vehicle'''
    system('cls')  # clears stdout
    vehicle = add_vehicle(vehicle_type)
    if vehicle != None:
        vehicles_list.append(vehicle)

def searchVehicle(vehicles_list):
    '''Function that lets the user search for a vehicle by name'''
    system('cls')  # clears stdout
    globals.search(vehicles_list, input('Find vehicle by name >>>'))

def showAllVehicle(vehicles_list):
    '''Shows all vehicles in the database'''
    print(f'\nThe following cars are in inventory ({len(vehicles_list)}):')
    for item in vehicles_list:
        print(item)

def showVehicleTickets(vehicles_list):
    '''Shows all the vehicle that got a ticket'''
    print('Checking DB for cars with speeding tickets')
    speedingtickets = speedTickets.listSpeeders(globals.BOX_A, globals.BOX_B, globals.SPEEDLIMIT, globals.STRETCH_LENGTH)
    speedTickets.speedTicketNew(vehicles_list, speedingtickets, globals.SPEEDLIMIT)
    speedTickets.speedTicket(vehicles_list)

def quit(vehicles_list):
    '''Exiting the program and sorting the database'''
    globals.sort_list(vehicles_list)
    system('cls')
    print('Exiting the program...')
    sys.exit()

# Call the main function.
if __name__ == '__main__':
    main()
