class Employee:

    data=[
            {"id":1,"name":"jhon","dept":"hr","salary":34000},
            {"id":2,"name":"hari","dept":"it","salary":24000},
            {"id":3,"name":"ravi","dept":"qa","salary":64000},
            {"id":4,"name":"vijay","dept":"hr","salary":74000},
            {"id":5,"name":"tom","dept":"it","salary":24000},
            {"id":6,"name":"vipin","dept":"qa","salary":14000},
            
        ]




    def get(self,*args,**kwargs):
            return print(self.data)

    def retrive(self,*args,**kwargs):
          id=kwargs.get("id")
            #dictionary name(kwargs)
          record=[emp for emp in self.data if emp.get("id")==id] 
          return record
    
    def create(self,*args,**kwargs):
          self.data.append(kwargs)
          return self.data

    def distroy(self,**kwargs):
          id=kwargs.get("id")
          obj=[e for e in self.data if e.get("id")==id][0]
          return self.data.remove(obj)


    def updation(self,id=None,*args,**kwargs):
          id=id
          obj=[ emp for emp in self.data if emp.get("id")==id][0]
          obj.update(kwargs)
          print("employee object updated")
          return obj

          

obj=Employee()
# print(obj.get())

# print(obj.retrive(id=3))

# obj.create(id=7,name="vishnu",dept="hr",salary=24000)

obj.distroy(id=2)
obj.get()

# print(obj.get())
 
# obj.updation(id=4,name="hani",salary=60000)
           #(   kwargs                    )
# print(obj.retrive(id=4))
