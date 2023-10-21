s=input("enter a string: ")
l=len(s)
s1=""
for i in range(0,l):
    s1=s1+s[4-i]
print("is the string palindrome: ")
print(s == s1)