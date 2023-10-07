class Parent:
    vehicle=["activa","wangonr"]

    def properties(self):
        return self.vehicle
    
class child(Parent):
    def properties(self):
        self.vh= super().properties()
        self.vh.append("gt")
        return self.vh
    
ch=child()
print(ch.properties())