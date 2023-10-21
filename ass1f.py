s1=input("enter string 1: ")
s2=input("enter string 2: ")
l2=len(s2)
l1=len(s1)
k=0
p=0
if l1!=l2:
    print("wrong data given")
else:
    for i in range (0,l1):
        if s1[i]==s2[p]:            
            k=k+1
        else:
            p=p+1
    if k==0:
        print("the two input strings are an anagram of eachother")
    else:
        print("the two input strings are not an anagram of eachother")
    