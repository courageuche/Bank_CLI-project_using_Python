from bankcli import Account
from Savings import Savings
if __name__ == '__main__':
    #Driver code
    Bank_account = Account("Full name:", "Date of birth:", "Phone number:", "email:", "2084506548", 0, "Openning balance:", "Enter desired pin:", "Enter new pin:",) # create an object of class
    His = Savings("Full_name: ", "Date of birth: ", "Phone number: ", "email: ", "2084506548", 0, "Openning balance: ", "Enter desired pin: ", "Enter new pin: ")# create an object of child class
    
    print("default pin is 101") 
    default = int(input("Enter the default pin: "))
    if default == 101:
        decision = "1"
        while decision == "1":
            print("1.Open account \n 2. Check account balance \n 3. Change Pin \n 4. Deposit \n 5. Withdraw \n 6. Transfer \n 7. Calculate monthly interest")
            select_option = int(input("Enter any option above: "))
            if select_option == 1:
                print("8. Savings account \n 9. Current account")
                New_account = int(input("enter any option above: "))
                if New_account == 8:
                    Bank_account.open_account1()#calling functions with that class
                elif New_account == 9:
                    Bank_account.open_account2()#calling functions with that class
            elif select_option == 4:
                His.deposit()#calling functions with that class
            

