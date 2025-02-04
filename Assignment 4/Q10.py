sent=input("Enter string: ")
x=sent[0]
s=sent[0]+sent[1:].replace(sent[0],"$")
# c=0
# for ch in sent:
#     if ch == x:
#         if c>0:
#             s+='$'
#         else:
#             s+=ch
#         c+=1
#     else:
#         s+=ch

print(s)