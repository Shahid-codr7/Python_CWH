s='Hello, hi i am abcd'
s1=s.split()[-1]
last2=s1[:2]
print(last2)
print(s.find('hello'))

s2=''
for i in s:
    if(i.isupper()):
        s2=s2+i.lower()
    else:
        s2=s2+i.upper()
print(s2)
# 0R
print(s.swapcase())

print(s.split(','))
print(s.replace(' ',','))
print(s.replace('Hello','Hi'))

b='balloon door'
st=b[0]
for i in range(1,len(b)):
    if(b[i-1]==b[i]):
        st=st+'*'
    else:
        st=st+b[i]
print(st)

sentence1='hi people, hello'
sentence=sentence1.split()
sent=''
for i in sentence:
    sent=sent+i.capitalize()+" "
print(sent)