class Vehicle:
    def move(self):
        pass  

class Car(Vehicle):
    def move(self):
        return "Driving "

class Plane(Vehicle):
    def move(self):
        return "Flying "

class Boat(Vehicle):
    def move(self):
        return "Sailing "


vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
