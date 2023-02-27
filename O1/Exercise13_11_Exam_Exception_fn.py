# From paperback edition
# Different from Revel!!
# The revel exercise is about the Triangle class...
class ExamException(Exception):
    def __init__(self, score):
        super().__init__()
        self.__score = score
    def getScore(self):
        return self.__score

class NegativeResultException(ExamException):
    def __init__(self, score):
        super().__init__(score)
    
class ExcessiveResultException(ExamException):
    def __init__(self, score):
        super().__init__(score)


class Exam:
    def __init__(self, name:str, score:int) -> None:
        if score < 0:
            raise NegativeResultException(score)
        elif score > 100:
            raise ExcessiveResultException(score)
        self.__name = name
        self.__score = score
    def __str__(self):
        return f'Navn = {self.__name}, score = {self.__score}'

def main():
    try:
        #exam1 = Exam("John",-1)
        exam2 = Exam("Paul",101)

    except NegativeResultException as ex:
        print(f'Error, the score is negative, {ex.getScore()}')
    except ExcessiveResultException as ex:
        print(f'Error, the score is greater than 100, {ex.getScore()}')
    exam3 = Exam("Peter",95)
    print(exam3)

main()