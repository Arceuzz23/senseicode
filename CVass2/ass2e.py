import numpy as np
a=np.random.randint(0,69 ,size=(4,4))
a=a.astype('float64')
b=np.zeros((4,1))
s=0
print("original array: ")
print(a)
for i in range(0,4):
    for j in range (0,4):
        s=a[i,j]+s
    b[i,0]=s/4
for i in range(0,4):
    for j in range (0,4):
        a[i,j]=a[i,j]-b[i,0]
print("final array: ")
print(a)
