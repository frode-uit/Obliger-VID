#Car, Truck and SUV Demo
# Roy Espen Olsen og Hallgeir Johnsen
import vehicles
import SpeedTicket
import os
import pickle
from datetime import datetime

def file_to_dictionary(filename):
    file_dictionary = {}
    file = open(filename, "r")
    for line in file:
        license, time = line.split(", ")
        file_dictionary[license] = time.replace("\n", "")
    file.close()

    return file_dictionary

def actual_speed(distance, time):
    speed = (distance / time) * 3600
    return speed

def list_speeders(filename_a, filename_b, speed_limit, distance):
    list_of_speeders = {}
    allowed_speed = speed_limit * 1.05
    time_format = '%Y-%m-%d %H:%M:%S'

    dictionary_a = file_to_dictionary(filename_a)
    dictionary_b = file_to_dictionary(filename_b)
    
    try:
        for licence in dictionary_a:
            if licence in dictionary_b:
                box_a_time = datetime.strptime(dictionary_a[licence], time_format)
                box_b_time = datetime.strptime(dictionary_b[licence], time_format)

                time_from_a_to_b = (box_b_time - box_a_time).total_seconds()
                avg_speed = actual_speed(distance, time_from_a_to_b)

                if avg_speed > allowed_speed:
                    list_of_speeders[licence] = (format(avg_speed, ".3f"), dictionary_a[licence])

    except ValueError:
        print("Error in function 'list_speeders': Wrong format in .txt-file, please use '%Y-%m-%d %H:%M:%S' for time.\nExample: 2022-01-03 07:11:41")

    return list_of_speeders

def new_vehicle_input():
    licence = input("Please enter licence number: ")
    make =    input("Please enter make and model of car: ")
    year =    input("Please enter year of the make: ")
    milage =  input("Please enter milage of the car: ")
    price =   input("Please enter the price of the new car: ")
    info = f'{licence}, {make}, {year}, {milage}, {price}'
    return info.split(", ")

NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
SHOW_TICKETS = 6
QUIT_CHOICE = 7

def main():
    try:
        savefile = "list_of_vehicles.dat"
        
        if os.path.isfile(savefile):
            dat_of_vehicles = open(savefile, "rb")
            vehicles_list = pickle.load(dat_of_vehicles)
            dat_of_vehicles.close()
        else:
            vehicles_list = []
        
        box_a = "box_a.txt"
        box_b = "box_b.txt"
        speed = 60
        distance = 5

        if os.path.isfile(box_a) and os.path.isfile(box_b):
            list_of_speeders = list_speeders(box_a, box_b, speed, distance)

            for car in vehicles_list:
                license = car.get_license_number()
                
                if license in list_of_speeders.keys():
                    if list_of_speeders[license] not in car.get_tickets_str():
                        date_and_time = list_of_speeders[license]
                        ticket = SpeedTicket.speedTicket(license, date_and_time)
                        car.append_ticket(ticket)
            
        choice = 0
        while choice != QUIT_CHOICE:
            display_menu()
            choice = int(input('Enter your choice: '))

            if choice == NEW_CAR_CHOICE:
                print("\nAdd  a new car")

                info = new_vehicle_input()
                new_car = vehicles.Car(info[0], info[1], int(info[2]), int(info[3]), float(info[4]),
                    int(input("Please enter number of doors: ")))
                vehicles_list.append(new_car)

            elif choice == NEW_TRUCK_CHOICE:
                print("\nAdd a new truck")

                info = new_vehicle_input()
                new_car = vehicles.Truck(info[0], info[1], int(info[2]), int(info[3]), float(info[4]),
                    input("Please enter drivetype(front/rear-wheel or 4WD): "))
                vehicles_list.append(new_car)

            elif choice == NEW_SUV_CHOICE:
                print("\nAdd a new SUV")

                info = new_vehicle_input()
                new_car = vehicles.SUV(info[0], info[1], int(info[2]), int(info[3]), float(info[4]),
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

            elif choice == SHOW_TICKETS:
                print('\nThe following cars got speeding tickets:')
                
                for car in vehicles_list:
                    if len(car.get_tickets()) > 0:
                        print(f'License: {car.get_license_number()}, Speeding ticket: {car.get_tickets_str()}')
                                
            elif choice == QUIT_CHOICE:
                print('Exiting the program...') 

                sorted_vehicle_list = sorted(vehicles_list, key = lambda car: car.get_make())
                
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
    print('6) Show tickets')
    print('7) Quit')     

if __name__ == '__main__':
    main()