# Sets in python are unordered and contain only unique data
s={}
print(type(s)) # Output:  <class  'dict'>
s={2,4,2,'wre',5,6,4,23}
print(s)
print(type(s))
s.add(9)
print(s)
name='hello'
s.update(name)
print(s)

print('popped out:',s.pop()) # Pops  out any random element from the set
print(s)

s.remove(9)
print('removed 9')
print(s)

t={3,45,2,1,'ko',23,5,34}
print('intersection')
print(t.intersection(s))

print('union')
print(t.union(s))

print('difference')
py={'hulk','ironman','superman'}
jv={'cap am','hawkeye','ironman','superman'}
print(py.difference(jv))
print(jv.difference(py))

