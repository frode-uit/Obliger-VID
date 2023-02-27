#Vehicle

class Vehicle:
    def __init__(self, license_number, make, year, milage, price):
        self._license_number = license_number.upper()
        self._make = make
        self._year = year
        self._milage = milage
        self._price = price
        self._speed_tickets = []

    @property
    def licence_number(self):
        return self._licence_number
    
    @licence_number.setter
    def licence_number(self, licence_number):
        self._licence_number = licence_number

    def append_ticket(self, ticket):
        self._speed_tickets.append(ticket)

    def get_tickets(self):
        return self._speed_tickets

    def get_tickets_str(self):
        self._ticket_strings = []
        for ticket in self._speed_tickets:
            self._ticket_strings.append(ticket.get_ticket())
        return self._ticket_strings

    def __str__(self):
        info = f'License: {self._license_number},  Make:  {self._make},  Year: {self._year},  Milage:  {self._milage},  Price:  {self._price}'
        return info

class Car(Vehicle):
    def __init__(self, license_number, make, year, milage, price, number_of_doors):
        super().__init__(license_number, make, year, milage, price)
        self._number_of_doors = number_of_doors

    
    def __str__(self):
        return super().__str__() + f', Number of Doors:  {self._number_of_doors}'

class Truck(Vehicle):
    def __init__(self, license_number, make, year, milage, price, drivetype):
        super().__init__(license_number, make, year, milage, price)
        self._drivetype = drivetype

    
    def __str__(self):
        return super().__str__() + f', Drivetype: {self._drivetype}'

class SUV(Vehicle):
    def __init__(self, license_number, make, year, milage, price, passenger_capacity):
        super().__init__(license_number, make, year, milage, price)
        self._passenger_capacity = passenger_capacity

    
    def __str__(self):
        return super().__str__() + f', Number of Passengers: {self._passenger_capacity}'
