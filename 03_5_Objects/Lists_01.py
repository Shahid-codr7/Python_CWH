l=list()
print(type(l))
l=[1,2,3,'abcdefg',7.7,'virat',True]
print(l[-1])
print(l[-len(l)])
print(l[0:5:2])
#  indexing same as string in python
print('indexing same as string in python')
print(l[3])
print(l[3][1])
print(l[3][1:5])
print(l[5])
print(len(l))
print('Reversed List: ',l[::-1])

# lists are mutable. id() remains same even after changing elements. Like Dictionaries and sets. Unlike  strings,  tuples, int, float, etc.


print('# lists are mutable. id() remains same even after changing elements. Like Dictionaries and sets. Unlike  strings,  tuples, int, float, etc.')

print(l)
print(id(l))
l[0]=-1
print(l)
print(id(l))

# id of another new list
print('# id of another new list')

l1=[1,2,3,"",0,]
print(l1)
print(id(l1))
l1[3]=3
print(l1)
print(id(l1))

# id for elements in list is different as they are separately immutable eg. string , int,etc.
print('# id for elements in list is different as they are separately immutable eg. string , int, etc.')
print(id(list[0]))
print(id(list[2]))

#  list is iterable just like string
print('list is iterable just like string')
for i in l:
    print(i,end=' ')
