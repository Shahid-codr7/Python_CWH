list1 = list('abcd')
print(list1)
# ERROR : list2 = list(123)  print(list2)
b=[67,54,32.6,43,67]
print(b.count(67))
print(b.index(67))
# print(b.find(67))
print(b.pop())
print(b)
b.sort()
print(b)
b.insert(1,'Jonny')
print(b)
# Deletion in Lists
print('Deletion in Lists')
print(b)
b[1:3]=[]
print(b)
b.insert(2,'Cr_07') 
print(b)
b.remove(54)
print(b)
b.insert(1,'Jonny') 
b.insert(3,70)
print(b)
del b[2:4]
print(b)
del b[2] 
del b
#print(b)  error

# Append and Extend
print('Append')
l=[1,2,4,'cr7',99]
print(l)
l.append('rahul')
print(l)
l.append(796)
print(l) 
l1=[5,6,7]
l.append(l1)
print(l)
l.extend(l1)
print(l)
s='ronaldo'
l.extend(s)
print(l)
