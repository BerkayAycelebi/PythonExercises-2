
from ast import While


class gallery:
    car_name="Passat"
    km=9500
    color="Kırmızı"
    def car_properties(self):
        print(f"Car name:{self.car_name}\nKm: {self.km}\nColor Info:{self.color}")

y=gallery()
y.car_properties()

class School:
    def __init__(self,branch,teacher,department,class_size,salary):
        self.branch=branch
        self.teacher=teacher
        self.department=department
        self.class_size=class_size
        self.salary=salary

    def show_info(self):
        print("*"*50)
        print("Clas Information")
        print("Branch: {}\nTeacher: {}\nDepartmant:{}\nClass Size:{}\n".format(self.branch,self.teacher,self.department,self.class_size))
        print("*"*50)

    def changeDepartmant(self):
        new_department=input("Please enter new department")
        print("*"*50)
        print("Eski Bölüm:",self.department)
        self.department=new_department
        print("*"*50)
        print("Clas Information")
        print("Branch: {}\nTeacher: {}\nDepartmant:{}\nClass Size:{}\n".format(self.branch,self.teacher,self.department,self.class_size))
        print("*"*50)

    def showSalary(self):
        print(f"{self.teacher} name of tearcher salary is:{self.salary}")



class Manager(School):
    print("Manager Panel")
    def __init__(self,branch,teacher,department,class_size,salary,seniority):
        super().__init__(branch,teacher,department,class_size,salary)
        self.seniority=seniority


        # self.branch=branch
        # self.teacher=teacher
        # self.department=department
        # self.class_size=class_size
        # self.seniority=seniority


    def show_info(self):
        print("*"*50)
        print("Manager Information")
        print("Branch: {}\nTeacher: {}\nDepartmant:{}\nClass Size:{}\nSeniority:{}\n".format(self.branch,self.teacher,self.department,self.class_size,self.seniority))
        print("*"*50)

    def increaseSalary(self):
        print(f"Welcome to increase salary panelmr/mrs {self.teacher}")
        increaseAmount=int(input("Enter inscreased amount"))
        self.salary=int(self.salary)+increaseAmount
        print(f"Increasing amount of  {self.teacher} is {increaseAmount}")
        print(f"Current salary is {self.salary}")
    
# mn=Manager("11C","Mehmet","Fizik","35","5000","Baş müdür")
# mn.increaseSalary()

class_name=input("Please enter branch name")
teacherInfo=input("Enter teacher name")
department_name=input("Enter department name")
class_size=input("enter class size")
salaryTake=input("Enter a salary")

print("If you are manager fill in this place")
seniorTake=input("Enter a seniority")
if not seniorTake:
    print("Teacher Mode")

CreateClass=input("Enter a class name")

while True:
    if not seniorTake:
        CreateClass=School(class_name,teacherInfo,department_name,class_size,salaryTake)
        print("class Created")
        y=input("1-Show Info\n-Show Salary\n3-Change Department\n")
        if y=="1":
            CreateClass.show_info()
        elif y=="2":
            CreateClass.showSalary()
        elif y=="3":
            CreateClass.changeDepartmant()
        else:
            break
    else:
        CreateClass=Manager(class_name,teacherInfo,department_name,class_size,salaryTake,seniorTake)
        print("class Created")
        y=input("1-Show Info\n2-Insceacse Salary\n3")
        if y=="1":
                CreateClass.show_info()
        elif y=="2":
                CreateClass.increaseSalary()
        else:
            break
            







    







