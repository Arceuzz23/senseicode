import numpy as np
a=np.ones((10,10))
pr=np.random.randint(0,10 ,size=(1,3))
pc=np.random.randint(0,10 ,size=(1,3))
p=np.random.randint(1,69, size=(1,3))
for i in range(0,3):
    a[pr[0,i],pc[0,i]]=p[0,i]
print(a)