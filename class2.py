class BankAccount:
    acc_no=501020000
    def __init__(self):
        self.ano=BankAccount.acc_no
        BankAccount.acc_no+=1

    def open_account(self):
        self.name=input("Enter The Name:-").title()
        self.balance=float(input('Enter opening Balance:-'))
        print(f'congratulations ,your Ac_No:-{self.ano}')
    
    def deposit(self):
        Amt=float(input("Enter The Amount:-"))
        self.balance=+Amt
        print(f"{amt} is Deposited")
    
    def withdraw(self):
        Amt=float(input('Enter The Amount:-'))
        if self.balance >=Amt:
            self.balance=-Amt
            print(f"{Amt} is Withdraw")
        else:
            print('Insufficient Balance')
    
    def Display(self):
        print(f'Account_No:- {self.ano} \
            \n Name:-        {self.name}\
            \n Balance:-     {self.balance}')

    def get_ano(self):
        return self.ano

#End Of Class
accts=[]
while True:
    print("-"*30)
    print(f"1.Open account\n 2.Deposit\n 3.Withdraw\
        \n4.Display\n0.Exit")
    choice=input("Enter Choice")
    if not choice or not choice.isdigit():
        print('Invalid Choice')
        continue

    choice=int(choice)
    if choice==0:
        print("Good Bye")
        break

    elif choice==1:
        b=BankAccount()
        b.open_account()
        accts.append(b)

    elif 2<=choice<=4:
        ano=int(input('Enter Account Number'))
        for b in accts:
            if b.get_ano()==ano:
                if choice==2:
                    b.deposit()
                    break
                elif choice==3:
                    b.withdraw()
                    break
                else:
                    b.Display()
                    break
        else:
            print(f'{ano} is invalid Ac_No')
    else:
        print("Invalid choice")

    
    
