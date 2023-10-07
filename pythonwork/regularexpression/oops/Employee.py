class Employee:
    id:int
    name:str
    dipartment:str
    gender:str

    def create(self,id,name,department,gender):
        self.id=id
        self.name=name
        self.dipartment=department
        self.gender=gender
    def display_emp(self):
        print(self.id,self.name,self.department,self.gender)

    