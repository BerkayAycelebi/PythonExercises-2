import sqlite3

db=sqlite3.connect("Credit_Book.db")

authority=db.cursor()
while True:
    print("***WELCOME TO CREDIT BOOK***")
    authority.execute("CREATE TABLE IF NOT EXISTS people(name,amount)")
    panel=input("1-Add Credit:\n2-Look At Credits")
    if panel=="1":
        creditName=input("Please enter a name of credit")
        creditAmount=input("Please enter a credit amount")
        authority.execute(f"INSERT INTO people VALUES('{creditName}','{creditAmount}')")
        db.commit()
        print(f"Credit name of person is: {creditName}")
        input("Contunie?")
    elif panel=="2":
        authority.execute("SELECT *FROM people")
        datas=authority.fetchall()
        y=1
        for item in datas:
            print(f"{y}. Credit name: {item[0]}\nCredit Amount:{item[1]}\n")
            y+=1
        input("Contunie?")





