import time
try:
     x=int(input("Number 1"))
     y=int(input("Number 2"))
     division=x/y
     print(division)
except (ZeroDivisionError,ValueError):
    print("Error")
    
finally:
     ctn=5
     for i in range(5):
          time.sleep(1)
          print("Countdown:",ctn)
          ctn-=1
     print("Completed")





     print("Process is completed")
   