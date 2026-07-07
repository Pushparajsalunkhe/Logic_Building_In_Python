class emp:
    Emp_No=1
    def __init__(self):
        self.emp_no=emp.Emp_No
        emp.Emp_No+=1
    
    def Detais_emp(self):
        self.name=input('Enter The Emp_Name:-').title()
        self.age=int(input('Enter The Age:-'))
        self.Position=input('Enter The Emp_Position(HR/Emp):-')
        self.salary=int(input("Enter The Salary:-"))
        print(f'congratulations ,your Emp_No:-{self.emp_no}')

    def Salary_in(self):
        ince=int(input('Enter The  Salery increment in percent:-'))
        self.temp_salary=self.salary*ince/100
        print(f'{self.temp_salary} is increment')
        self.salary+=self.temp_salary


    def display (self):
         print(f"Name:-{self.name}\
            \n Age:-{self.age}\
            \n Position:-{self.Position}\
            \n Salary:-{self.salary}")

    def get_emp(self):
        return self.emp_no

a=[]
while True:
    print('_'*30)
    print(f"1.Detais_Emp\n 2.Salary_increment\n 3.Display\n 0.Exit")
    choice=int(input('Enter The Choice:-'))
    
    if choice==0:
        print('!..Good Bye..!')
        break
    elif choice==1:
        b=emp()
        b.Detais_emp()
        a.append(b)
    elif 2<= choice <=3:
        emp=int(input("Enter The Emp_No:-"))
        for b in a:
            if b.get_emp()==emp:
                if choice==2:
                    b.Salary_in()
                    break
                else:
                    b.display()
                    break
        else:
            print("Invalid Emp_NO")
    else:
        print('Invalid choice')


        
        