class Car:
    total_car =0
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand+" !"
    def full_name(self):
        return (f"{self.brand} {self.model}")
    def fuel_type(self):
        return "Petrol or Disel"
    
my_Safari=Car("Tata","Safari")
my_Nexon=Car("Tata","Nexon")
my_Indica=Car("Tata","Indica")

print(Car.total_car)



