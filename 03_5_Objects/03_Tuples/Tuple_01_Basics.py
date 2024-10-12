t=(1,2,3,5,"Earth",9.9)
print(type(t)) 
t1=('a',97,9.8,'abs')
print(t1)
print(t1[1])   
print(t1[-1])   
print(t1[1:3])   
# Error: t[1]='b'  Tuples are immutable

T=()
print(type(T))
a=tuple()
print(type(T))
print(T)
T=(1)
print(type(T))  # Output: <class 'int'>

a=(1,)
print(a)  # Output:  (1,)
print(type(a))  # Output: <class 'tuple'>
print(len(a))

b=tuple("Ronaldo")
print(b)  # Output: ('R', 'o', 'n', 'a', ...
print(len(b))  

c=([76,'abc'])
print(c)  # Output: [76, 'abc']
print(type(c))   # Output: <class 'list'>

d=([76,'abc'],)
print(d)  # Output: ([76, 'abc'],)
print(type(d))    # Output: <class 'tuple'>
print(type(d[0]))    # Output: <class 'tuple'>
print(len(d))

# Lists inside a Tuple can be changed as they are individual objects 
e=(76,'abc',[1,2,3])
print(e)  # Output: (76, 'abc', [1, 2, 3])
e[2][1]='abcd'
print(e)   # Output: (76, 'abc', [1, 'abcd', 3])

# Unpacking a Tuple
a, b = 1, 4
print(a,b)

t=(1,3,2,4,'ronaldo')
a, b, c, d, e = t # This is known as 'Unpacking a Tuple'
print(a,b,c,d,e)  # Output: 1 3 2 4 ronaldo