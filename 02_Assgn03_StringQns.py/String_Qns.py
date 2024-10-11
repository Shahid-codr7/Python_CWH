def star():
    s=input('Enter string : ')
    res=''
    if len(s)==0:
        return ''
    else:
        res+=s[0]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                res=res+'*'
            else:
                res=res+s[i]    
    print(res)

