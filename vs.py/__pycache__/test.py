class student:
    def __init__(self):
        pass
    def dip(self):
        self.rno=rno
        self.name=name
        self.marks=marks
    def ditiles(self):
        rno=int(input("Enter The RollNo Number:"))
        name=input("Enter The Name:")
        marks=float(input("Enter The marks"))
    def display(self):
        print(f"Rno={self.rno}\
            \n Name={self.name}\
            \n Marks={self.marks}")
s1=student()
s1.ditiles()
s1.dip()
s1.display()
