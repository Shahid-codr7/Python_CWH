import sys
l=[]
print("Enter 10 double values ")
minimum=sys.maxsize
for i in range(10):
    l.append(float(input("Enter a double value: ")))
    if minimum > l[i]:
        minimum=l[i]
print("Minimum: ",minimum)

