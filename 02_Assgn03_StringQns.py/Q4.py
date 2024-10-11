def maxChar(s):
    max=-1
    f=0
    for i in s:
        if s.count(i)>max:
            max=s.count(i)
            maxchar=i
            f=1
    if(f==1):
        return maxchar
    else:
        return ''
    
def main():
    s=input("Enter string : ")
    maxc=maxChar(s)
    s1=s.replace(maxc,'-')
    print(s1)

if __name__ == "__main__":
    main()