class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return self.__brand+" !"
    def full_name(self):
        return (f"{self.brand} {self.model}")
    def fuel_type(self):
        return "Petrol or Disel"
    
class ElctricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric "
    
class Battery:
    def battery_info(self):
        return "this is a battery"

class Engine:
    def engine_info(self):
        return "this is a engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla =ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
