class vehicle:
    def __init__(self, brand, year, km, price, regno):
        self.brand          = brand
        self.year           = year
        self.km             = km
        self.price          = price
        self.regno          = regno
        self.speedticket    = set()
    
    def __str__(self):
        return f'Registration number: {self.regno}, Vehicle Brand: {self.brand}, Year: {self.year}, Km: {self.km}, Price: {self.price}'

class Car(vehicle):
    def __init__(self, brand, year, km, price, doors, regno):
        super().__init__(brand, year, km, price, regno)
        self.doors = doors
    
    def __str__(self):
        return super().__str__() + f' Doors: {self.doors}'

class Truck(vehicle):
    def __init__(self, brand, year, km, price, drive, regno):
        super().__init__(brand, year, km, price, regno)
        self.drive = drive
    
    def __str__(self):
        return super().__str__() + f' Drive: {self.drive}'

class SUV(vehicle):
    def __init__(self, brand, year, km, price, cap, regno):
        super().__init__(brand, year, km, price, regno)
        self.cap = cap
    
    def __str__(self):
        return super().__str__() + f' Capacity: {self.cap}'

def add_vehicle(what_type):
    '''Takes the type of vehicle as input and after some questions returns the correct vehicle'''
    name = input('Enter a brand and model name >>> ')
    model_year = (input('Enter model/year >>> '))
    price = (input('Enter the price >>> '))
    km = (input('Enter the km >>> '))
    regno = (input('Enter Registration number (AB12345) >>> '))
    if(name == '' or model_year == '' or price == '' or km == '' or regno == ''):
        print('Not enough data, please try again')
        return
    # Select what type of vehicle it is
    if what_type == 1:
        special = input('Enter number of doors >>> ')
        return Car(name, model_year, km, price, special, regno)
    elif what_type == 2:
        special = input('Enter drive(FWD, RWD, 4WD) >>> ')
        return Truck(name, model_year, km, price, special, regno)
    else:
        special = input('Enter the capacity >>> ')
        return SUV(name, model_year, km, price, special, regno)
