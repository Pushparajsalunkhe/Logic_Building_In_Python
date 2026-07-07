class student:
    Reg_No=102022000
    def __init__(self):
        self.reg=student.Reg_No
        student.Reg_No +=1


    def stu_details(self):
        self.name=input('Enter The Name:-').title()
        self.cast=input('Enter The Cast:-').title()
        self.ssc=float(input('Enter The SSC Marks:-'))
        self.hsc=float(input('Enter The HSC Marks:-'))
        self.cet=float(input('Enter The CET Marks:-'))
        print(f"Congratulations,Your Reg_No is:-{self.reg}")
       
        
    def dispy(self):
        print(f'Name:-{self.name}\
            \n Cast:-{self.cast}\
            \n SSC Marks:-{self.ssc}\
            \n HSC Marks:-{self.hsc}\
            \n CET Marks:-{self.cet}')
    def get_reg(self):
        return self.reg

#End Of Class
accts=[]       
while True:
    print("-"*30)
    print(f' 1.Student_Details \n2.Disply \n 0.Exit')
    choice=input("Enter the choice:-")
    if not choice or not choice.isdigit():
        print("Invalid choice")
        continue
    choice=int(choice)
    if choice==0:
        print("Good Bye")
        break
    elif choice==1:
        b=student()
        b.stu_details()
        accts.append(b)

    elif choice==2:
        reg=int(input('Enter Reg_N0 Number:-'))
        for b in accts:
            if b.get_reg()==reg:
                if choice==2:
                    b.dispy()
                    break
                else:
                    print("no data found")
                    break
        else:
            print('Reg_no is Invalid')
        
    else:
        print('Invalid choice')
        
        

        
