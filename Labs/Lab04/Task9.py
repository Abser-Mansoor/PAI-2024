class Student :
    def __init__(self, stdid, name) :
        self.stdid = stdid
        self.name = name

    def print_student(self) :
        print([self.stdid, self.name])

class Marks(Student) :
    def __init__(self, stdid, name, algo, DataScience, cal) :
        super().__init__(stdid, name)
        self.algo_marks = algo
        self.DataScience_marks = DataScience
        self.cal_marks = cal

    def print_marks(self) :
        print([self.algo_marks, self.DataScience_marks, self.cal_marks])

class Result(Marks) :
    def __init__(self, stdid, name, algo, DataScience, cal) :
        super().__init__(stdid, name, algo, DataScience, cal)

    def print_result(self) :
        print(f"Total Marks: {self.algo_marks + self.DataScience_marks + self.cal_marks}\nAverage Marks: {(self.algo_marks + self.DataScience_marks + self.cal_marks)/3}")

res = Result("23K-0030","Abser",70,80,90)
res.print_student()
res.print_marks()
res.print_result()
