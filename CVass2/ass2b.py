import numpy as np
a1=input("enter the number of rows: ")
a2=input("enter the number of columns: ")
b1=int(a1)
b2=int(a2)
x = np.ones((b1,b2))
print("Original array:")
print(x)
for i in range (0,b1):
    for j in range (0,b2):
        if (i+j)%2==0:
            x[i,j]=0
print("The checkbox patternex array: ")
print(x)

