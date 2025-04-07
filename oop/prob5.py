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
    
my_tesla=ElctricCar("Tesla","Model S","85kWH")
print (my_tesla.fuel_type())
my_Safari=Car("Tata","Safari")
print(my_Safari.fuel_type())