b='balloon door'
st=b[0]
for i in range(1,len(b)):
    if(b[i-1]==b[i]):
        st+='*'
    else:
        st+=b[i]
print(st)