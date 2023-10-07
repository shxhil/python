class Calculator:
    def add(self,n1,n2):
        return n1+n2
    
    def add(self,n1,n2,n3):
        return n1+n2+n3
    
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4       #exicute this only bcz line by line exicution in python , latest will select
    

obj=Calculator()
obj.add(10,12)

#to overcome using *
#eg= *args