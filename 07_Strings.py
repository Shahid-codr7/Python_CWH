str="Harry"
length=len(str)
print(length)

s=input("Naam daalo: ")
n=9
print("good morning!",s,n,657) #by comma single space
print("good morning!"+s+" hi")   #by concatenation
print(f"good morning!{s} balle balle {s}") #by f string


letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
latter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

date=input("Date daal:",)
name=input("naam daalo:",)

#Normal
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)

#Alternative(Chaining)
print(latter.replace("<|Name|>",name).replace("<|Date|>",date))



# #Finding double space
st="heello ji  awaaz arahi hai "
c=st.find(" ")
print(c)

print(st[3])
