class Student:
    rollnumber:int
    name:str
    course:str
    gender:str

    def create(self,rollno,name,course,gender):
        self.rollnumber=rollno
        self.name=name
        self.course=course
        self.gender=gender
    def display_emp(self):
        print(self.rollnumber,self.name,self.course,self.gender)
    
obj=Student()
obj.create(20,"shahil","bca","male")
obj.display_emp()