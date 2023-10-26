import numpy as np
a=np.arange(1,6)
b=np.zeros((1,17))
print(a)
for i in range (0,17):    
    if i%4==0:
        z=i/4        
        b[0,i]=a[int(z)]
    else:
        b[0,i]=0
print(b)
