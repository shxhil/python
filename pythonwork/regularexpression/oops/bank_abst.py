from abc import ABC,abstractmethod

class bankingapp(ABC):
    @abstractmethod
    def fundtransaction(self):
        pass

    @abstractmethod
    def balanceEnquiry(self):
        pass
    
    @abstractmethod
    def transactionhistory(self):
        pass

class gpay(bankingapp):
    def fundtransaction(self):
        print("transaction using gpay")

    def balanceEnquiry(self):
        print("enquiry using gpay")

    def transactionhistory(self):
        print(" history using gpay")

obj=gpay()
obj.balanceEnquiry()
obj.fundtransaction()