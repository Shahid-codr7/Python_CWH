def maxchar(s):
    maxch=s[0]
    maxc=s.count(s[0])
    for i in s[1:]:
        if maxc<s.count(i):
            maxc=s.count(i)
            maxch=i
    print(s.replace(maxch,"-"))
maxchar('ABBHGBBHHHHGSC')