from bankcli import Account
from sqlconnect import mydb

class Current(Account): #inheritance class - child class
    def __init__(this, full_name, date_of_birth, phone_number, email, account_number, account_balance, oppening_bal, account_pin, new_pin):
        super(). __init__(full_name, date_of_birth, phone_number, email, account_number, account_balance, oppening_bal, account_pin, new_pin)
        
    def acc_balance(this): #A methhod
        acc_no = input("Enter the Account number: ")

        #SQL query
        #create a variable to pick balance field from ammount_1 table
        d1 = ("SELECT * FROM ammount_2 WHERE Acc_no = %s")

        #Make a tuple of the field account number
        Data_ = (acc_no,)

        #Create a cursor object
        B = mydb.cursor()
        B.execute(d1, Data_)#Execute the query

        result = B.fetchone()#find just one balance record i.e in same row with the account no
        print("Balance for account:", acc_no, "is", result[-1] )
        

    def change_pin(this): #A method
        pin_setup = int(input("Enter your previous pin: "))
        pin_setup2 = int(input("Enter your desired pin: "))
        #SQL query
        #create a variable to pick balance field from ammount_1 table
        d1 = ("SELECT pin FROM account_2 WHERE pin = %s")

        #Make a tuple of the field account number
        Data_ = (pin_setup,)

        #Create a cursor object
        B = mydb.cursor()
        B.execute(d1, Data_)#Execute the query

        result = B.fetchone()#find just one balance record i.e in same row with the account no
        t = pin_setup2
        sql = ("UPDATE account_1 SET pin = %s WHERE pin = %s")
        z = (t, pin_setup)

        B.execute(sql, z)
        mydb.commit()

        print("Pin changed successfully")

    def deposit(this): #A method
        ammount = int(input("Enter ammount to be deposited: ")) 
        acc_no = input("Enter the Account number: ")
        
        #SQL query
        #create a variable to pick balance field from ammount_1 table
        d1 = ("SELECT balance FROM ammount_2 WHERE Acc_no = %s")
        
        #Make a tuple of the field account number
        Data_ = (acc_no,)

        #Create a cursor object
        B = mydb.cursor()
        B.execute(d1, Data_)#Execute the query
        
        result = B.fetchone()#find just one balance record i.e in same row with the account no
        t = result[0] + ammount
        sql = ("UPDATE ammount_2 SET balance = %s WHERE Acc_no = %s")
        z = (t, acc_no)
        
        B.execute(sql, z)
        mydb.commit()

        print("You have successfully depositd:", ammount)
    
    def withdraw(this): #A method
        ammount = int(input("Enter ammount to be deposited: ")) 
        acc_no = input("Enter the Account number: ")
        
        #SQL query
        #create a variable to pick balance field from ammount_1 table
        d1 = ("SELECT balance FROM ammount_2 WHERE Acc_no = %s")
        
        #Make a tuple of the field account number
        Data_ = (acc_no,)

        #Create a cursor object
        B = mydb.cursor()
        B.execute(d1, Data_)#Execute the query
        
        result = B.fetchone()#find just one balance record i.e in same row with the account no
        t = result[0] - ammount
        sql = ("UPDATE ammount_2 SET balance = %s WHERE Acc_no = %s")
        z = (t, acc_no)
        
        B.execute(sql, z)
        mydb.commit()

        print("You have successfully withdrawn:", ammount)
    
    
