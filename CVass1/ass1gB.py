import array
s=input("enter a string: ")
s1=s.lower()
l=len(s1)
lt=["*"]*l
for i in range(0,l):
    for j in range(i+1,l):
        if s1[i]==s1[j]:
            lt[i]=s1[i]
            break
    
for i in range(0,l):
    for j in range(i+1,l):
        if lt[i]==lt[j]:
            lt[j]="*"    
print("The duplicate letters in the string are: ")
for i in range (0,l):
    if ((lt[i]!="*")or(lt[i]!=" ")):
        print(lt[i])
    
    
