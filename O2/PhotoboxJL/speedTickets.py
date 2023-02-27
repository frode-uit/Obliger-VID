from datetime import datetime
from globals import fileToDictionary

class SpeedTicket:
    def __init__(self, regno, date_time, speed, speedlimit):
        self.regno      = regno
        self.date_time  = date_time
        self.speed      = speed
        self.speedlimit = speedlimit
        self.key        = date_time + regno

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self) -> str:
        return f'\t\t\tDate and Time: {self.date_time}, Speed Limit: {self.speedlimit}, Registered speed: {self.speed}'

def speedTicketNew(v_list, ticketdict, speedlimit):
    '''Adds new tickets to the cars needs: vehicles list, dict with tickets and speedlimit'''
    for v in v_list: 
        if v.regno in ticketdict:
            speed, date_time = ticketdict[v.regno]          
            v.speedticket.add(SpeedTicket(v.regno, date_time, speed, speedlimit))

def speedTicket(v_list):
    '''Needs a vehicle list to check for tickets'''
    for v in v_list:
        if len(v.speedticket) > 0:
            print(f'\n{v}')
            for ticket in v.speedticket:
                print(ticket)

def listSpeeders(filename_a, filename_b, speed_limit, distance):
    '''filename needs complete filename with file extension (text.txt), speed_limit is in KM/H, distance is KM'''
    speeders = {}
    file_a = fileToDictionary(filename_a)
    file_b = fileToDictionary(filename_b)
    # Calculating speedlimit with +5%
    speedlimit = speed_limit * 1.05
    f = ' %Y-%m-%d %H:%M:%S'
    for key in file_a:
        if key in file_b:
            d_time = datetime.strptime(file_b[key], f) - datetime.strptime(file_a[key], f)
            velocity = ((distance * 1000) / d_time.total_seconds()) * 3.6
            if velocity > speedlimit:
                speeders[key] = (round(velocity, 3), file_a[key])
    return speeders