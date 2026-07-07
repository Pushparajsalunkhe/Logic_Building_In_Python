class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def disply(self):
        print("hii",self.name)
        print('your marks are',self.marks)
    def grade(self):
        if(marks>=60):
            print('your are in first grade')
        elif(marks>=50):
            print('your are in second grade')
        elif(marks>=40):
            print('your are in third grade')
        else:
            print("your are failed")

name=input('Enter name')
marks=int(input('Enter marks'))
s=student(name,marks)
s.disply()
s.grade()