import random
import globals
from vehicles import Car, Truck, SUV

def generateCars():
    car_list = []
    v_dict = globals.fileToDictionary(globals.BOX_A)
    cars = {'Volvo': {'car': {'S60', 'S90', 'V60'}, 'SUV': {'ZC40', 'XC60', 'XC90'},},
            'Volkswagen': {'truck': {'Amarok', 'Crafter Pickup', 'Transporter Pickup'}, 'car': {'Golf', 'Passat', 'Jetta'}, 'SUV': {'ID4', 'T-Cross', 'T-Roc'}},
            'Toyota': {'truck': {'Hilux', 'Tacoma', 'Tundra'}, 'car': {'Agya', 'Supra', 'Yaris'}, 'SUV': {'RAV 4', 'C-HR', 'Yaris Cross'}},
            'Ford': {'truck': {'F-150 Raptor', 'Maverick', 'Lobo'}, 'car': {'Fiesta', 'Focus', 'Kuga'}, 'SUV': {'Puma', 'Kuga', 'Explorer'}},
            'BMW': {'car': {'X1', '325', '318'}, 'SUV': {'X1', 'X2', 'X4'}},
            'Audi': {'car': {'A1', 'A3', 'A4'}, 'SUV': {'Q5', 'Q7', 'Q8'}},
            'Kia': {'car': {'Ceed', 'EV6', 'K8'}, 'SUV': {'Sorento', 'Seltos', 'Sonet'}},
            'Renault': {'truck': {'Alaskan'}, 'car': {'Clio', 'Espace', 'Kadjar'}, 'SUV': {'Austral', 'Koleos', 'Captur'}},
            'Mercedes-Benz': {'car': {'CLA', 'CLS', 'EQE'}, 'SUV': {'EQE SUV', 'EQA', 'EQB'}},
            'Peugeot': {'truck': {'Landtrek'}, 'car':{'208', '301', '308'}, 'SUV': {'3008', '2008', '5008'}}
            }
    for regno in v_dict:
        # Makes random choises for the brand, model and type
        brand = random.choice(list(cars))
        v_type = random.choice(list(cars[brand]))
        car = random.choice(list(cars[brand][v_type]))
        # Appending the choices into the correct class object
        if regno not in car_list:
            if v_type == 'car':
                car_list.append(Car(f'{brand} {car}', random.randint(2011, 2023), 
                                        random.randint(0, 200000), random.randint(15000, 900000), 
                                        random.choice([2, 4]), regno))
            elif v_type == 'truck':
                car_list.append(Truck(f'{brand} {car}', random.randint(2011, 2023), 
                                        random.randint(0, 200000), random.randint(15000, 900000), 
                                        random.choice(['FWD', 'RWD', '4WD']), regno))
            elif v_type == 'SUV':
                car_list.append(SUV(f'{brand} {car}', random.randint(2011, 2023), 
                                        random.randint(0, 200000), random.randint(15000, 900000), 
                                        random.choice([2, 3, 4, 5]), regno))
        else:
            pass
        
    return car_list