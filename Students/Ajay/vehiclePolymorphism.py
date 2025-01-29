class BMW:
    def fuel_type(self):
        print("the fuel type of a BMW is premium gasoline")
    def max_speed(self):
        print("the max speed of a BMW is 302 km/h")
class Ferrari:
    def fuel_type(self):
        print("the fuel type of a ferrari is premium gasoline")
    def max_speed(self):
        print("the max speed of a ferrari is 330 km/h")
obj_ferrari = Ferrari()
obj_BMW = BMW()
for i in (obj_BMW, obj_ferrari):
    i.fuel_type()
    i.max_speed()