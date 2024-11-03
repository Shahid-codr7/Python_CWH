d={
    'Apple': 124,
    'Orange':99,
    "Grapes":0,
    "Banana":40,
}
print(d)
print(d['Apple'])
print(d["Orange"])

# get(<key>,a):  To avoid error, it returns a

print(d.get('Banana'))
print(d.get('Lichi','Not avaliable'))
print(d.get('Lichi',-1.0))

# updating  dictionary with  new value or with a nested dictionary
# Dictionary has a key-value pair. It can be any object like string, int as well as tuple, list, dictionary as a value in it. Key must be unique and immutable (e.g., strings, numbers, tuples)

print(d) 
print('updating  dictionary') 
d['Banana']={'long': 777, 'short':  500}
print(d)
d["Apple"]=("Kashmiri",'Gujarati')
print(d)
d[0]=["Kashmiri",'Gujarati']
print(d)

# update()
D={7:'seven', 4:'chouka'}
print(D)
d.update(D)
print(d) 

# Citizenship check 

print('Apple' in d)  # True
print("guava" in d)   # False

# Deletion
# pop() : It removes the item with the specified key and returns the value of the item.
# popitem() : It removes the last inserted item from the dictionary.
# clear() : It removes all items from the dictionary.
print('Deletion')
d={'Apple': 124, 'Orange':99, "Grapes":0}
print(d)
print(d.pop('Apple'))   # 124
print(d)  # {'Orange': 99, 'Grapes': 0}
print(d.popitem())   # ('Grapes', 0)
print(d)  # {'Orange': 99}
print(d.popitem()) # {'Orange': 99}
print(d)

# iterable
# dict.keys() : It returns a view object that displays a list of all keys available in the dictionary
# dict.values() : It returns a view object that displays a list of all values available in the dictionary
# dict.items() : It returns a view object that displays a list of a tuples of all key-value pairs in dictionary



d={'Apple': 124, 'Orange':99, "Grapes":0}
print(d.keys())  # dict_keys(['Apple', 'Orange', 'Grapes'])
print(d.values())  # dict_values([124, 99, 0])
print(d.items())   # dict_items([('Apple', 124), ('Orange', 99), ('Grapes', 0)])

for i in d:
    print(i,d[i])    # Apple 124 Orange 99 Grapes 0
    # OR
for key, value in d.items():
    print(key,value)  # Apple 124 Orange 99 Grapes 0







