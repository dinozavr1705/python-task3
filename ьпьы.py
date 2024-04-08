from щклмл import Car
from щклмл import list_of_all_cars
car=Car("Camri","?",30039230)
class Profile:
    def __init__(self,username,password,description,balance):
        self.username = username
        self.decription = description
        self.__password = password
        self.balance = balance
    @property
    def username(self):
        return self.username

    @username.setter
    def username(self,username2):
        self.username = username2

    @property
    def descrtiption(self):
        return self.decription

    @descrtiption.setter
    def descrtiption(self,new_description):
        self.decription = new_description

    def print_profile(self):
        print(f"username:{self.username} description:{self.decription}")


class User(Profile):
    def buy_car(self,cost):
        if self.balance >= cost:
            print("машина была успешно куплена")
            self.balance-= cost
        else:
            print("не хватает средств")

class Admin(User):
    def add_car(self,car):
        list_of_all_cars(car)
        with open("list_of_all_cars.txt","r") as file:
            file.write(list_of_all_cars)

admin = Admin("admin","admin123","just admin",648725873467586475643876578678536)
user = User("user","user123","just user",0)