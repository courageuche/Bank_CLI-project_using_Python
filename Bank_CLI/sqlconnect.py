import mysql.connector

#ESTABLISH DATABASE CONNECTION
def dat():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Courage@0621",
    database="bank_account"
    )

    return mydb