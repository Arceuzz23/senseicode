dic={}
l=input("enter the length of dictionary: ")
l1=int(l)
lk=[0]*int(l)
lv=[0]*int(l)
lv1=[0]*int(l)
print("key is the left hand side quantity")
key=input()
print("value is the right hand side quantity")
value=input()
print("enter the values for the dictionary: ")
for i in range(int(l)):
    lk[i]=input()
    lv[i]=input()
    dic[key]=value
lv=list(set(lv))
lv.sort()
print("the sorted list of unique values is: " + str(lv))

    


    

