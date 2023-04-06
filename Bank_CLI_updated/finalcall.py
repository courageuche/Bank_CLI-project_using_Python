from bankcli import Account
from Savings import Savings
from current import Current

if __name__ == '__main__':
    #Driver code
    Bank_account = Account("Full name: ", "Date of birth: ", "Phone number: ", "email:", "2084506548", 0, "Openning balance:", "Enter desired pin:", "Enter new pin:",) # create an object of class
    His = Savings("Full_name: ", "Date of birth: ", "Phone number: ", "email: ", "2084506548", 0, "Openning balance: ", "Enter desired pin: ", "Enter new pin: ")# create an object of child class
    Her = Current("Full_name: ", "Date of birth: ", "Phone number: ", "email: ", "2084506548", 0, "Openning balance: ", "Enter desired pin: ", "Enter new pin: ")# create an object of child class

    print("default pin is 101")
    default = int(input("Enter the default pin: "))
    if default == 101:
        decision = "1"
        while decision == "1":
            print("1. Open account \n 2. perform operation")
            select_option = int(input("Enter any option above: "))
            if select_option == 1:
                print("3. Savings account \n 4. Current account")
                New_account = int(input("enter any option above: "))
                if New_account == 3:
                    Bank_account.open_account1()#calling functions with that class
                elif New_account == 4:
                    Bank_account.open_account2()#calling functions with that class
            elif select_option == 2:
                print("5.Savings account \n 6. Current account")
                operation1 = int(input("enter any option above: "))
                if operation1 == 5:
                    print("7. check balance \n 8. Change Pin \n 9. Deposit \n 10. Withdraw \n 11. Calculate monthly interest")
                    operation2 = int(input("enter any option above: "))
                    if operation2 == 7:
                        His.acc_balance()#calling functions with that class
                    if operation2 == 8:
                        His.change_pin()#calling functions with that class
                    elif operation2 == 9:
                        His.deposit()#calling functions with that class
                    elif operation2 == 10:
                        His.withdraw()#calling functions with that class
                elif operation1 == 6:
                    print("7. check balance \n 8. Change Pin \n 9. Deposit \n 10. Withdraw \n 11. check charges")
                    operation3 = int(input("enter any option above: "))
                    if operation3 == 7:
                        Her.acc_balance()#calling functions with that class
                    if operation3 == 8:
                        Her.change_pin()#calling functions with that class
                    elif operation3 == 9:
                        Her.deposit()#calling functions with that class
                    elif operation3  == 10:
                        Her.withdraw()#calling functions with that class





            
                
                
                
               