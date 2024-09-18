import abc
from abc import *

class Student:
    def __init__(self,id_num,name) :
        self.std_id = id_num
        self.name = name
    def printdata(self) :
        print(f"Student id is {self.std_id}\nStudent name is {self.name}")

class Class_Marks(Student):
    def __init__(self,algo,DS,calc,id_num,name) :
        super().__init__(id_num,name)
        self.algo_marks = algo
        self.DS_marks = DS
        self.calculus_marks = calc

    def printmarks(self) :
        print(f"Algo marks are {self.algo_marks}\nDS marks are {self.DS_marks}\nCalculus marks are {self.calculus_marks}")

class Class_Result(Class_Marks) :
    def __init__(self,algo,DS,calc,id_num,name) :
        super().__init__(algo,DS,calc,id_num,name)
    
    def printresult(self) :
        print(f"Total marks are {self.algo_marks+self.DS_marks+self.calculus_marks}\nAverage is {(self.algo_marks+self.DS_marks+self.calculus_marks)/3}")
        

res = Class_Result(80,85,90,"10332993","Abser")
res.printresult()
