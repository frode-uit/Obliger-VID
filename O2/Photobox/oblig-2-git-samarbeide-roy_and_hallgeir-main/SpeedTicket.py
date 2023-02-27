#SpeedTicket

class speedTicket:
    def __init__(self, licence_number, avg_speed_time_tuple):
        self.__licence_number = licence_number
        self.__tuple = avg_speed_time_tuple

    def set_licence_number(self, licence_number):
        self.__licence_number = licence_number

    def get_licence_number(self):
        return self.__licence_number

    def set_ticket(self, avg_speed_time_tuple):
        self.__tuple = avg_speed_time_tuple       

    def get_ticket(self):
        return self.__tuple