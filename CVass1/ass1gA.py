import array
s=input("enter a string: ")
s1=s.lower()
s2=s1.split()
l1=len(s2)
s3=""
for i in range(0,l1):
    s3=s3+s2[i]
l=len(s3)
lt=["*"]*l
for i in range(0,l):
    for j in range(i+1,l):
        if s3[i]==s3[j]:
            lt[i]=s3[i]
            break
for i in range(0,l):
    for j in range(i+1,l):
        if lt[i]==lt[j]:
            lt[j]="*"   
print("The duplicate letters in the string are: ")
for i in range (0,l):
    if lt[i]!="*":
        print(lt[i]),