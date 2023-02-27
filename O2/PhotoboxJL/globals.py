import pickle

# Constants for the menu choices
NEW_CAR_CHOICE          = 1
NEW_TRUCK_CHOICE        = 2
NEW_SUV_CHOICE          = 3

# Constants for the files, speedlimit and stretch length
BOX_A           = 'box_a.txt'
BOX_B           = 'box_b.txt'
SPEEDLIMIT      = 60
STRETCH_LENGTH  = 5
VEHICLE_DB      = 'vehicles.db'

def sort_list(v_list):
    '''Sorts the list upon exiting the program and dumping the content into a database'''
    with open(VEHICLE_DB, 'wb') as fp:
        v_list.sort(key=lambda brand_name: brand_name.brand)
        pickle.dump(v_list, fp)

def search(v_list, name):
    '''Search function to find a vehicle, spliting the brand name and matches the keyword against the name 
    Can altso search for model name of car'''
    print(f'\n     Search results for {name.upper()}')
    for v_brand in v_list:
        v_name = v_brand.brand.split(' ')
        for i in range(len(v_name)):
            if v_name[i].upper() == name.upper():
                print(v_brand)

def fileToDictionary(filename):
    '''Use the complete name with file extension (text.txt)'''
    passings = {}
    with open(filename, 'r') as fp:
        for line in fp:
            key, data = line.rstrip('\n').split(',')
            passings[key] = data
    return passings