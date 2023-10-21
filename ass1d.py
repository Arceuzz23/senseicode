n=input("enter the nth term: ")
a=0
b=1
c=0
print("the fibonacci series is:")
print(a)
for i in range(0, int(n)-1):
    a=b
    b=c
    c=a+b
    print(c)
