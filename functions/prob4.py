import math
def circle_stat(radius):
    area= math.pi*radius**2
    circumference = 2*math.pi*radius
    return round(area,2),round(circumference,2)

print(circle_stat(5.07))