class Student:
    id:int   #instant variable
    name:str
    age:str
    course:str

    def __init__(self,id,name,age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print(self.name,self.course)

    def __str__(self):
        return self.id

obj1=Student(20,"shahil",21,"bca")
# obj1.display()
print(obj1)