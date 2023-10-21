dic={}
k=0
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
lv.sort()
for i in range(0,l1):
    for j in range(i+1,l1):
        if lv[i]==lv[j]:
            lv1[i]=lv[j]
        else:
                lv1[i]=lv[i]
                k=1+k

if k==(l1*(l1-1))/2:
     for i in range(0,l1):
          print(lv[i])
else:
     for i in range(0,l1):
          print(lv1[i])
     

    


    

