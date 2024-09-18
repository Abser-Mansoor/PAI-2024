import abc
from abc import *

class Account:
    def __init__(self,number,balance,code) :
        self.__account_no = number
        self.__account_bal = balance
        self.__security_code = code
    def printdata(self) :
        print(f"Account number is {self.__account_no}\nAccount balance is {self.__account_bal}\nSecurity Code is {self.__security_code}")

acc = Account("03352225666",1000,'42101')
acc.printdata()
