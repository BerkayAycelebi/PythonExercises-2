from ast import While
import subprocess as sp
password="12345"
userpassword=input("Please enter your password")

if userpassword==password:
    while True:
         print("***Welcome To Aplication***")
         makeChoose=input("1-Notepad\n2-Calculator")

         if makeChoose=="1":
            sp.call("notepad.exe")
            input("continue")
         elif makeChoose=="2:":
            sp.call("calc.exe")
            input("continue")


       