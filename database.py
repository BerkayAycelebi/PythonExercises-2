import sqlite3

db=sqlite3.connect("books.db")

authority=db.cursor()

bookname=input("Enter a book name")
pageCount=input("Enter page count")
year=input("enter book year")


authority.execute("CREATE TABLE IF NOT EXISTS book (name,pageCount,year)")
authority.execute(f"INSERT INTO book VALUES('{bookname}','{pageCount}','{year}')") 
authority.execute("SELECT *FROM book WHERE year='2020'")
write_data=authority.fetchall()
# write_data=authority.fetchmany(2) herhangi veriyi çeker
for item in write_data:
    print(f"Book name: {item[0]}\nPage Count: {item[1]}\nBook Year: {item[2]}\n")



db.commit()
db.close()