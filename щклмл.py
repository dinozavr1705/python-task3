from abc import abstractmethod
class Car:
    def __init__(self,name,model,cost):
        self.name = name
        self.model = model
        self.cost = cost
        self.car = {"name":self.name,"model":self.model,"cost":self.cost}
    def print_car(self):
        print(f"название:{self.name} модель:{self.model} цена:{self.cost}")
with open("list_of_all_cars.txt","r") as file:
 list_of_all_cars =file
