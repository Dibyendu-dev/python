class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return (f"{self.brand} {self.model}")
    
class ElctricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size


my_tesla=ElctricCar("Tesla","Model S","85kWH")
print(my_tesla.model)
print(my_tesla.full_name())
