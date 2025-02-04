lst=[]

while(True):
    lst.append(int(input("Enter element: ")))
    if(lst[-1]==0):
        break

l=[]
# for i in range(101):
#     l.append(0)
# for i in lst:
#     l[i]+=1
# for i,count in enumerate(l):
#     if(i!=0 and count!=0):
#         print(f"{i} occurs {count} times")

for i in lst:
    if i not in l:
        print(f'{i} occurs {lst.count(i)} times')
        l.append(i)

