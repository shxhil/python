class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    @property    #avoid  brackets
    def get_name(self):
        return self.name
    

    @property
    def get_age(self):
        return self.age
    

obj=Student("shahil",21)
print(obj.get_name)