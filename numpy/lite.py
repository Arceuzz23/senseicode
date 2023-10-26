import numpy as np
a=np.array([1,5,0,0,53,78,4,0,21,79,0,4,5,17])
for i in range (0,14):
  s=a[1,i]
  if s!=0:
    print("The indices of non-zero elements: ")
    print(a[1,i])