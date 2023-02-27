#Vehicle

class Vehicle:
    def __init__(self, license_number, make, year, milage, price):
        self.__license_number = license_number.upper()
        self.__make = make
        self.__year = year
        self.__milage = milage
        self.__price = price
        self.__speed_tickets = []

    def set_license_number(self, license_number):
        self.__license_number = license_number

    def get_license_number(self):
        return self.__license_number

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def set_milage(self, milage):
        self.__milage = milage

    def get_milage(self):
        return self.__milage

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def append_ticket(self, ticket):
        self.__speed_tickets.append(ticket)

    def get_tickets(self):
        return self.__speed_tickets

    def get_tickets_str(self):
        self.__ticket_strings = []
        for ticket in self.__speed_tickets:
            self.__ticket_strings.append(ticket.get_ticket())
        return self.__ticket_strings

    def __str__(self):
        info = f'License: {self.__license_number},  Make:  {self.__make},  Year: {self.__year},  Milage:  {self.__milage},  Price:  {self.__price}'
        return info

class Car(Vehicle):
    def __init__(self, license_number, make, year, milage, price, number_of_doors):
        super().__init__(license_number, make, year, milage, price)
        self.__number_of_doors = number_of_doors

    def set_number_of_doors(self, number_of_doors):
        self.__number_of_doors = number_of_doors

    def get_number_of_doors(self):
        return self.__number_of_doors

    def __str__(self):
        return super().__str__() + f', Number of Doors:  {self.__number_of_doors}'

class Truck(Vehicle):
    def __init__(self, license_number, make, year, milage, price, drivetype):
        super().__init__(license_number, make, year, milage, price)
        self.__drivetype = drivetype

    def set_drivetype(self, drivetype):
        self.__drivetype = drivetype

    def get_drivetype(self):
        return self.__drivetype

    def __str__(self):
        return super().__str__() + f', Drivetype: {self.__drivetype}'

class SUV(Vehicle):
    def __init__(self, license_number, make, year, milage, price, passenger_capacity):
        super().__init__(license_number, make, year, milage, price)
        self.__passenger_capacity = passenger_capacity

    def set_passenger_capacity(self, passenger_capacity):
        self.__passenger_capacity = passenger_capacity

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def __str__(self):
        return super().__str__() + f', Number of Passengers: {self.__passenger_capacity}'
