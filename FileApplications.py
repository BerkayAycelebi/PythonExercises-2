import codecs
from hashlib import new

file_name=input("Please enter a file name you want create")
file_name_ext=file_name+".txt"
putData=input(f"Please add the file of {file_name_ext} to data")

with codecs.open(file_name_ext,"w",encoding="utf-8") as file:
    file.write(putData)
    adding=input("Do u want to data at file? Y/N").lower()
    if adding=="y":
        open(file_name_ext,"a")
        new_data=input("Please enter a data that you want add")
        new_data="\n"+new_data
        file.write(new_data)
        print("Datas added")
    else:
        print("loged out")

info=codecs.open(file_name_ext,"r",encoding="utf-8")
a=info.read()
print("***File of Datas***")
print(a)
