class Parent:

    phone="samsung"
    vehicle="gt"

    def mobile(self):
        print(self.phone)

    
    def bike(self):
        print(self.vehicle)

class Child(Parent):
    pass

obj=Child()
obj.mobile()
obj.bike() 

object #parrent class of all class