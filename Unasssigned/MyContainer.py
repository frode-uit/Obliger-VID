class MyContainer:
    def __init__(self,init_value = 0):
        self.__container = [init_value]*3
        self.__index = 0
    
    def put(self, value):
        self.__container[self.__index] = value
        if self.__index == 2:
            self.__index = 0
        else:
            self.__index += 1
    
    def __str__(self):
        return f'{[elem for elem in self.__container]}'
        #return str(self.__container[0])
           
    def __iter__(self):
        self.current_index = 0
        return self
    
    def __next__(self):
        if self.current_index <= 2:
            element = self.__container[self.current_index]
            if self.current_index == 2:
                self.current_index = 0
            else:
                self.current_index += 1
            return element
        else:
            raise StopIteration

my_container = MyContainer()
print(my_container)
my_container.put(1)
my_container.put(2)
my_container.put(3)
print(my_container)

for elem in my_container:
    print(elem) 