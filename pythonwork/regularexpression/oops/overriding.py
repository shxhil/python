class Bike:
    def start(self):
        print("kick start")
    def breaking(self):
        print("drum break")

class Herohonda(Bike):
    def start(self):
        print("self start")

    def breaking(self):
        print("abs break")

obj=Herohonda()
obj.breaking()
obj.start()

#vehicle
