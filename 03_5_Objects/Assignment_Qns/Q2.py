import random
n=5
l=[]
s=0
for i in range(n):
    l.append(random.randint(0,n))
    s+=l[i]
avg=int(s/n)
print(l,"\n",avg)
print(f"sum: {s}\navg: {avg}")
odd=[i for i in l if i%2!=0]
even=[i for i in l if i%2==0]
print(odd," | ",even)
print(f"odd: {odd}\neven: {even}")

