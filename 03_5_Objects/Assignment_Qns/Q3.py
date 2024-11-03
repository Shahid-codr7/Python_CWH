
lst=[]
c=0
while(True):
    lst.append(int(input("Enter element: ")))
    if(lst[c]==0):
        break
    c+=1
l=[]
for i in range(101):
    l.append(0)
for i in lst:
    l[i]+=1
for i,count in enumerate(l):
    if(i!=0 and count!=0):
        print(f"{i} occurs {count} times")