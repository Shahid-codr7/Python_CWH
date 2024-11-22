def main():
    l1=inputList()
    l2=inputList()
    print(l1)
    print(l2)
    print(mergeList(l1,l2))

def inputList():
    l=[]
    n=int(input("Enter size of array: "))
    for i in range(n):
        l.append(int(input("Enter:")))
    return l

def mergeList(l1,l2):
    l=[]
    for i in range(len(l1)):
        l.append(l1[i])
    for i in range(len(l2)):
        l.append(l2[i])
    print(sorted(l))
if __name__ == "__main__":
    main()