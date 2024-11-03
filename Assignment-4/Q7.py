st=input("Enter string: ")
s=st.split()
odd=0
even=0
for i in s:
    print(i)
    if len(i)%2==0:
        even+=1
    else:
        odd+=1
print(f"Odd: {odd}\nEven: {even}")

