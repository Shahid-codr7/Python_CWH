a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
l=[a,b,c]
print(l)
print(l[0])
print(l[0][0])
print(l[1][2])
for i in l:
    print(i)

for i in l:
    for j in i:
        print(j,end=',')
print()

l1=[]
for i in range(10):
    l1.append(i**2)
print(l1)

