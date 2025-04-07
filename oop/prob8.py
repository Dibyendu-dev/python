class Car:
    total_car =0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand+" !"
    def full_name(self):
        return (f"{self.__brand} {self.__model}")
    def fuel_type(self):
        return "Petrol or Disel"
    
    @staticmethod
    def general_description():
        return "car are means of transport"
    @property
    def model(self):
        return self.__model
    
my_Safari=Car("Tata","Safari")
print(my_Safari.general_description())
print(Car.general_description())
print(my_Safari.model)
