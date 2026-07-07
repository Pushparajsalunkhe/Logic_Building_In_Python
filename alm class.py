class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def manu(self):
        user_input=input('''
                           Hello, how would you link to proceed ?
                           1.Enter 1 to create pin
                           2.Enter 2 to deposit
                           3.Enter 3 to withdraw
                           4.Enter 4 to check balance
                           5 Enetr 5 to exit



''')
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance
        else :
            print("Bye")

            def create_pin(self):
                self.pin=int(input("Enter your pin"))
                print("pin set successfully")
            def deposit(self):
                temp=int(input("Enter your pin"))
                if temp==self.pin:
                    amount=int(input("Enter the amount"))
                    self.balance=self.balance+amount
                    print("Deposit successfully")
                else:
                    print("Invalid pin")
            def withdraw(self):
                temp=int(input("Enter your pin "))
                if temp==self.pin:
                    amount=int(input("Enter the amount"))
                    if amount<self.balance:
                        print("operation successfully")
                    else:
                        print("insufficient balacen ")
                else:
                    print("Invalid pin")
            def check_balance(self):
                temp=int(input("Enter your pin"))
                if temp==self.balance:
                    print(self.balance)
                else:
                    print("Invalid pin")
                                     
                               
        
   
