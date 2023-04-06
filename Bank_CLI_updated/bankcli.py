from sqlconnect import mydb
from numpy import random

class Account: #class declaration - Parent class
    def __init__(this, full_name, date_of_birth, phone_number, email, account_number, account_balance, oppening_bal, account_pin, new_pin): #method initializes the class
        this.full_name = full_name
        this.date_of_birth = date_of_birth
        this.phone_number = phone_number
        this.email = email
        this.account_number = account_number
        this.account_balance = account_balance
        this.oppening_bal = oppening_bal
        this.account_pin = account_pin
        this.new_pin = new_pin
        
    def open_account1(this): #A method
        Name = str(input(("{0}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin,)))
        DOB = str(input(("{1}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin)))
        this.phone_number = str(input(("{2}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.oppening_bal, this.account_balance, this.account_pin, this.new_pin)))
        phone = this.phone_number
        email = str(input(("{3}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin)))
        this.account_pin = int(input(("{7}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.oppening_bal, this.account_balance, this.account_pin, this.new_pin)))
        pin = this.account_pin
        this.oppening_bal = int(input(("{6}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin)))
        o_bal = this.oppening_bal
        bal = this.oppening_bal
        acc_no = 2011020302 + random.randint(211111, 255555)
        print(acc_no)
        print(this.account_pin)

        #Make a tuple
        Data1 = (Name, DOB, email, phone, pin, acc_no, o_bal)
        Data2 = (Name, acc_no, bal)

        #Write to mysql database
        sql1 =("INSERT INTO account_1 VALUES (%s, %s, %s, %s, %s, %s, %s)")
        sql2 = ("INSERT INTO ammount_1 VALUES (%s, %s, %s)")

        #Create a cursor object
        A = mydb.cursor()
        A.execute(sql1, Data1)
        A.execute(sql2, Data2)
        mydb.commit()

        print("Your account is created successfully")

    def open_account2(this): #A method
        Name = str(input(("{0}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin,)))
        DOB = str(input(("{1}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin)))
        this.phone_number = str(input(("{2}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.oppening_bal, this.account_balance, this.account_pin, this.new_pin)))
        phone = this.phone_number
        email = str(input(("{3}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin)))
        this.account_pin = int(input(("{7}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.oppening_bal, this.account_balance, this.account_pin, this.new_pin)))
        pin = this.account_pin
        this.oppening_bal = int(input(("{6}").format(this.full_name, this.date_of_birth, this.phone_number, this.email, this.account_number, this.account_balance, this.oppening_bal, this.account_pin, this.new_pin)))
        o_bal = this.oppening_bal
        bal = this.oppening_bal
        acc_no = 3011020302 + random.randint(211111, 255555)
        print(acc_no)
        print(this.account_pin)

        #Make a tuple of data entries
        Data1 = (Name, DOB, email, phone, pin, acc_no, o_bal)
        Data2 = (Name, acc_no, bal)

        #Write to mysql database
        sql1 = ("INSERT INTO account_2 VALUES (%s, %s, %s, %s, %s, %s, %s)")
        sql2 = ("INSERT INTO ammount_2 VALUES (%s, %s, %s)")

        #Create a cursor object
        A = mydb.cursor()
        A.execute(sql1, Data1)
        A.execute(sql2, Data2)
        mydb.commit()

        print("Your account is created successfully")
       
