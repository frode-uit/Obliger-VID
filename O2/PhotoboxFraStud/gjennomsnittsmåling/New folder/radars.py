from pickle import *
from datetime import datetime, timedelta

def fileToDictionary(filename: str):
    dictionary = {}
    fil = open(filename)

    for line in fil.readlines():
        (registration, time) = line.strip().split(', ')
        dictionary[registration] = time

    fil.close()
    
    return dictionary

def list_speeders(filename_a: str, filename_b: str, speed_limit: int, distance: int):
    return listSpeeders(filename_a, filename_b, speed_limit, distance)

def listSpeeders(filename_a: str, filename_b: str, speed_limit: int, distance: int):
    dictionary = {}
    dict_a = fileToDictionary(filename_a)
    dict_b = fileToDictionary(filename_b)

    for vehicle in dict_a:
        if vehicle in dict_b:
            time1 = datetime.fromisoformat(dict_a[vehicle])
            time2 = datetime.fromisoformat(dict_b[vehicle])
            difference = time2 - time1
            speed = distance/(difference.total_seconds()/3600)
            if speed >= 1.05 * speed_limit:
                dictionary[vehicle] = (float("%.3f" % speed), dict_a[vehicle])
    
    return dictionary

class SpeedTicket():
    def __init__(self, registration: str, time: str, speed: float, speed_limit: int):
        self.registration = registration
        self.time = time
        self.speed = speed
        self.speed_limit = speed_limit

    def check_time(self, time: str):
        return time == self.time
    
    def __str__(self):
        return self.registration + " driving " + str(self.speed) + " km/h in a " + str(self.speed_limit) + " km/h zone on " + str(self.time)