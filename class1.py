class emp:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def disply(self):
        print(f'Emp_id:   {self.emp_id}\
            \n  name:   {self.name}\
            \n  Salary:  {self.salary}')
        
emp_id=int(input("Enter the emp_id:-"))
name=input('Enter the name:-')
salary=int(input('Enter the salary:-'))
s=emp(emp_id,name,salary)
s.disply()

        

       

