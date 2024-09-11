class Account :
    def __init__(self) :
        self.__account_no = ""
        self.__account_balance = 0
        self.__security_code = ""

    def init(self, number, balance, code) :
        self.__account_no = number
        self.__account_balance = balance
        self.__security_code = code
    
    def print(self) :
        print(f"Account number: {self.__account_no}\nAccount Balance: {self.__account_balance}\nSecurity Code: {self.__security_code}")

Acc = Account()
Acc.init("23040", 2000, "4421")
Acc.print()
