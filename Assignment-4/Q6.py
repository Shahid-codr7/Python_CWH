sent=input("Enter sentence: ")
s1=''
for word in sent.split():
    word=word.lower()
    s1+=word.capitalize()+' '
print(s1)