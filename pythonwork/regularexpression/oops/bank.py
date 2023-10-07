from datetime import datetime


class Bank:

    bank_name:str
    acno:str
    person_name:str
    ac_type:str
    balance:str

    def create(self,bank,acno,p_name,account,bal):
        self.bank_name=bank
        self.acno=acno
        self.person_name=p_name
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited with {amount} avl balance is{self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed insufficent balance")
        else :
            self.balance-=amount
            print(f"your {self.bank_name}has been withdrawed {amount} on {datetime.today() }aval balance{self.balance}")

    def get_balance(self):
        print(f"your available balance is {self.balance}")

    

obj1=Bank()
obj1.create("sbi","1024","vijay","savings",4000)
# obj1.deposit(2000)
obj1.withdraw(100)
# obj1.get_balance()

obj2=Bank()
obj2.create("sbi","1025","john","savings",5000)
# obj2.withdraw(250)
# obj2.get_balance()
