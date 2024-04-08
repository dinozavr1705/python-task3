class Pet():
    def __init__(self,name,years_old):
        self.__name = name
        self.years_old = years_old
    @property
    def name(self):
     return self.__name

    @name.setter
    def name(self,name):
        self.name = name

    def display_info(self):
        print(f"кличка:{self.name}, возраст:{self.years_old} лет")

class Popugay(Pet):
    def say_something(self):
        print(f'{self.name} twit,twit!')

    @property
    def years_old(self):
        return self.__years_old

    @years_old.setter
    def years_old(self, years_old):
            self.__years_old = years_old

class Dog(Pet):
    @property
    def years_old(self):
        return self.__years_old

    @years_old.setter
    def years_old(self, years_old):
            self.__years_old = years_old

    def say_something(self):
            print(f"{self.name} wof wof")

Anton = Popugay("Anton", 19)
Anton.display_info()
Anton.say_something()
John = Dog("John",30)
John.display_info()
John.say_something()