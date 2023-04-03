from bankcli import Account
from sqlconnect import dat

class Savings(Account): #inheritance class - child class
    def __init__(this, full_name, date_of_birth, phone_number, email, account_number, account_balance, oppening_bal, account_pin, new_pin):
        super(). __init__(full_name, date_of_birth, phone_number, email, account_number, account_balance, oppening_bal, account_pin, new_pin)
        
    def acc_balance(this): #A methhod
        print(this.account_balance)

    def change_pin(this): #A method
        pin_setup = int(input("Enter your previous pin: "))
        print(pin_setup)
        while pin_setup != this.account_pin:
            this.new_pin = int(input("Enter the correct pin: " ))
        else:
            int(input("Enter your desired new pin: "))
        print("Pin changed")

    def deposit(this): #A method
        ammount = int(input("Enter ammount to be deposited: ")) 
        acc_no = str(input("Enter the Account number: "))
        
        #SQL query
        #create a variable to select balance from ammount_1 table
        d1 = "SELECT balance FROM ammount_1 WHERE Acc_no = %s"
        
        #Make a tuple of the data account number
        Data3 = (acc_no,)

        #Create a cursor object
        B = dat.cursor()
        B.execute(d1, Data3)#Execute the query
        
        result = B.fetchone()#find just one record i.e the in same row with the account no
        d2 = result[0] + ammount
        sql = ('UPDATE ammount_1 SET balance WHERE Acc_no = %s')
        z = (d2, acc_no)
        
        B.execute(sql, z)
        dat.commit()
        main()

        print("You have successfully depositd:", ammount)
    
    def withdraw(this): #A method
        ammount = float(input("Enter ammount to be withdrawn: "))
        if this.account_balance >= ammount:
            this.account_balance -= ammount
            print ("You successfully withdrew:", ammount)
            print("Your account balance is", this.account_balance)
        else:
            print ("Insufficient balance ")

    def transfer(this): #A method
        input("Enter account number: ")
        ammount = float(input("Enter ammount to be transfered: "))
        if this.account_balance >= ammount:
            this.account_balance -= ammount
            print("Transfer successful ")
        else:
            print("Insufficient balance")

    def Interest_rate(this): #A method
        P = int(input("Enter the principal ammount: "))
        R = 20
        T = 0.08333
        Monthly_interest = (P*R*T) / 100
        print("interest for this month is: ", Monthly_interest)


