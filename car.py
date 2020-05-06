class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70


    def drive(self, distance):
        fuel = self.fuel * 10 / distance
        if fuel >= 1:
            self.__add_distance(True, distance)
            self.__substract_fuel(True, distance)
        else:
            self.__substract_fuel(False, distance)

    def __add_distance(self, check, distance):
        if check == True:
            self.odometr += distance


    def __substract_fuel(self, check, distance):
        if check == True:
            self.fuel -= distance / 10
            print('Let\'s drive!')
        else:
            print('Need more fuel, please, fill more!')


mine = Car('Toyota', 'Skyline', 2003)  

mine.drive(700)