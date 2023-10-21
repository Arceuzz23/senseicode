import math
print("enter sides of the triangle")
a=input("enter side A")
b=input("enter side B")
c=input("enter side C")
A=float(a)
B=float(b)
C=float(c)
if (A+B)>C or (B+C)>A or (C+A)>B :
    s=math.sqrt((A+B+C)/2)
    S=float(s)
    print(S)    
    area=math.sqrt(abs(S*(S-A)*(S-B)*(S-C)))
    print("the area of the triangle is: " + str(area))
else:
    print("wrong side lengths given")    
