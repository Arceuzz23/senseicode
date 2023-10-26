import numpy as np
a1=input("enter the number of rows: ")
a2=input("enter the number of columns: ")
b1=int(a1)
b2=int(a2)
x = np.ones((b1,b2))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:(b1-1),1:(b2-1)] = 0
print(x)