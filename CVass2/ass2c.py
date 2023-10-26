import numpy as np
a=np.arange(1,32)
b=np.array(["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
print("The calendar for October 2023 is: ")
for i in range (1,32):
    if i%7==0:
        print(a[i-1],b[6])
    if i%7==1:
        print(a[i-1],b[0])
    if i%7==2:
        print(a[i-1],b[1])
    if i%7==3:
        print(a[i-1],b[2])
    if i%7==4:
        print(a[i-1],b[3])
    if i%7==5:
        print(a[i-1],b[4])
    if i%7==6:
        print(a[i-1],b[5])