sent=input("Enter string: ")
x=input("Enter char: ")
s=''
c=0
for ch in sent:
    if ch == x:
        if c>0:
            s+='$'
        else:
            s+=ch
        c+=1
    else:
        s+=ch
print(s)