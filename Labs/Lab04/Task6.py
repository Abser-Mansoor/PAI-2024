class BankAccount :
    number = ""
    balance = 0
    DOO = ""
    name = ""
    def __init__(self,number, balance, DOO, name) :
        self.number = number 
        self.balance = balance 
        self.DOO = DOO 
        self.name = name
    
    def deposit(self, money, number, name, DOO) :
         if (number,name,DOO) == (self.number,self.name,self.DOO) :
             self.balance += money
             print(f"New Balance is {self.balance}")
             return
         print("Authorization Unsuccessful")
         return
    
    def withdraw(self, money, number, name, DOO) :
         if (number,name,DOO) == (self.number,self.name,self.DOO) and self.balance >= money :
             self.balance -= money
             print(f"New Balance is {self.balance}")
             return
         print("Authorization Unsuccessful")
         return
    
    def check_balance(self, number, name, DOO) :
        if (number,name,DOO) == (self.number,self.name,self.DOO) :
            print(f"Balance is {self.balance}")
            return
        print("Authorization Unsuccessful")
        return
    
Account = BankAccount("0193891", 1000, "4-12-1944", "Abser")
Account.deposit(200,"0193891", "Abser",  "4-12-1944")
Account.withdraw(2000,"0193891", "Abser",  "4-12-1944")
Account.withdraw(1000,"0193891", "Abser",  "4-12-1944")
Account.check_balance("0193891", "Abser",  "4-12-1944")
