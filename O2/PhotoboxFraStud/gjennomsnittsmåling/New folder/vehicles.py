from radars import SpeedTicket

class Vehicle:
    def __init__(self, make: str, model: int, mileage: int, price: float, registration: str):
        self.make = make
        self.model = int(model)
        self.mileage = int(mileage)
        self.price = float(price)
        self.registration = registration
        self.violations = []
    
    def get_make(self):
        return self.make
    
    def set_make(self, make):
        self.make = make
    
    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price

    def get_registration(self):
        return self.registration

    def set_registration(self, registration):
        self.registration = registration

    def add_violation(self, violation: SpeedTicket):
        self.violations.append(violation)
    
    def get_violations(self):
        return self.violations
    
    def __str__(self):
        return "Make: " + self.make + "  Model: " + str(self.model) + "  Mileage: " + str(self.mileage) + "  Price: " + str(round(self.price, 2)) + "  Registration: " + self.registration

class Car(Vehicle):
    def __init__(self, make: str, model: int, mileage: int, price: float, registration: str, doors: int):
        super().__init__(make, model, mileage, price, registration)
        self.doors = int(doors)
    
    def get_doors(self):
        return self.doors
    
    def set_doors(self, doors):
        self.doors = doors

    def __str__(self):
        return super().__str__() + "  Doors: " + str(self.doors)

class Truck(Vehicle):
    def __init__(self, make: str, model: int, mileage: int, price: float, registration: str, drive_type: str):
        super().__init__(make, model, mileage, price, registration)
        self.drive_type = drive_type
    
    def get_drive_type(self):
        return self.drive_type
    
    def set_drive_type(self, drive_type):
        self.drive_type = drive_type

    def __str__(self):
        return super().__str__() + "  Drive type: " + self.drive_type

class SUV(Vehicle):
    def __init__(self, make: str, model: int, mileage: int, price: float, registration: str, pass_cap: int):
        super().__init__(make, model, mileage, price, registration)
        self.pass_cap = int(pass_cap)
    
    def get_pass_cap(self):
        return self.pass_cap
    
    def set_pass_cap(self, pass_cap):
        self.pass_cap = pass_cap

    def __str__(self):
        return super().__str__() + "  Number of passengers: " + str(self.pass_cap)
