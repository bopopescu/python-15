class Calc:

    def add(self,num1,num2):
        return num1+num2

    def sub(self,num1,num2):
        return num1-num2

    def mul(self,num1,num2):
        return num1*num2

    def div(self,num1,num2):
        return num1/num2
    def calculate(self):
        Calc.num1=int(input("enter a number1 :"))
        print("type 1=addition")
        print("type 2=subtraction")
        print("type 3=multiplication")
        print("type 4=division")
        choice=input("type here :")
        Calc.num2=int(input("enter a number2 :"))
        if choice == "1":
            print(Calc.num1,"+",Calc.num2,"is",Calc.num1+Calc.num2)
        elif choice == "2":
            print(Calc.num1, "-", Calc.num2, "is", Calc.num1 - Calc.num2)
        elif choice == "3":
            print(Calc.num1, "*", Calc.num2, "is", Calc.num1 * Calc.num2)
        elif choice == "4":
            print(Calc.num1, "/", Calc.num2, "is", Calc.num1 / Calc.num2)


class Student:
    def __init__(self,fname,rollno,fathername,sex,std,city):
        self.fname=fname
        self.rollno=rollno
        self.fathername=fathername
        self.sex=sex
        self.std=std
        self.city=city

    def details(s1):
        dict={"firstname":s1.fname,
              "rollno":s1.rollno,
              "fathername":s1.fathername,
              "sex":s1.sex,
              "std":s1.std,
              "city":s1.city}
        for x,y in dict.items():
            print(x,":",y)
    def final1():
        print("*******Student details**********")
        fname=input("enter student first name:")
        rollno=input("enter student roll number:")
        fathername=input("enter student fathername:")
        sex=input("enter M/F :")
        std=input("enter student staandard:")
        city=input("enter student's city:")
        s1=Student(fname,rollno,fathername,sex,std,city)
        s1.details()

class Markscard:
    def __init__(self,sub1,sub2,sub3,sub4,sub5,sub6):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
        self.sub6 = sub6

    def grade(s1):
        avg=(s1.sub1+s1.sub2+s1.sub3+s1.sub4+s1.sub5+s1.sub6)/6
        per=(avg/600)*100
        if per>=90:
            print("Your grade:A")
        elif per>=80 or per<=90:
            print("your grade:B")
        elif per>=70 or per<=80:
            print("Your grade:C")
        elif per>=60 or per<=70:
            print("your grade:D")
        elif per>=50 or per<=60:
            print("Your grade:E")
        elif per<50:
            print("Your grade:F")

    def final():
        sub1=float(input("enter sub1 marks:"))
        sub2=float(input("enter sub2 marks:"))
        sub3=float(input("enter sub3 marks:"))
        sub4=float(input("enter sub4 marks:"))
        sub5=float(input("enter sub5 marks:"))
        sub6=float(input("enter sub6 marks:"))
        s1=Markscard(sub1,sub2,sub3,sub4,sub5,sub6)
        s1.grade()
def start():
    print("************************************************************************")
    print("type 1 for calculator")
    print("type 2 for  Student details")
    print("type 3 for Markscard details")
    choice = int(input("type here:"))
    if choice == 1:
        print("*****Calculator*****")
        x=Calc()
        x.calculate()
    elif choice == 2:
        Student.final1()
    elif choice == 3:
        Markscard.final()
    print("************************************************************************")
    start()

start()