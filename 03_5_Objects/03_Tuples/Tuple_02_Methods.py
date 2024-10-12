t=(1,6,4,'Earth',True)
print('count()')   # Output: 1
print(t.count('Earth'))   # Output: 1
print(t.count('ab'))   # Output: 1
print(t.count(True))   # Output: 2 coz  In Python, True is treated as 1 because of the way boolean values are implemented in the language. They are a subclass of integers, where True is equivalent to 1, and False is equivalent to 0.

print("index()")
print(t.index("Earth"))
print(t.index(True))   # True is equivalent to 1
print(t.index(6)) 

print('Iteration')   
for i in t:
    print(i*2,end=', ')   

print()
print("Concatenation")
t1=(1,2,3)
t2=t1+t
print(t2)
print(t2*2)

print('touple to list and list to tuple')
l=list(t)
print(l)
print(type(l))
T=tuple(l)
print(T)
print(type(l))




