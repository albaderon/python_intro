
class Vehicle:


    speed = 0
    passenger_capacity = 0
    fare = 0

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Name:", self.name)
        print("Speed:", self.speed)
        print("Passenger capacity:", self.passenger_capacity)
        print("Fare:", self.fare)


car = Vehicle("Car")
car.print_info()

print("Car", car.__dict__)



class Airbus(Vehicle):

    path_length = 1000

    def __init__(self,name):
        Vehicle.__init__(self,name)

    def time_way(self):
        time = self.path_length/self.speed
        return time


mriya = Airbus("Mriya")
mriya.speed = 1200
mriya.print_info()
print("Time:%.2f" % mriya.time_way())



class Train(Vehicle):

    number_of_vagons = 5

    def __init__(self,name):
        Vehicle.__init__(self,name)

    def passenger_in_vagon(self):
        pasengers = self.passenger_capacity/self.number_of_vagons
        return pasengers


hundiy_1 = Train("Hundiy 1")
hundiy_1.passenger_capacity = 500
hundiy_1.print_info()
print(hundiy_1.passenger_in_vagon())







