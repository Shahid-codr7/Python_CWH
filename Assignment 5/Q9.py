def duplicates(l):
    ND=[]
    n=len(l)
    for i in range(n):
        if l[i] not in ND:
            ND.append(l[i])
    return ND
def main():
    n=int(input('Enter n:'))
    print("Enter ",n," nos. ")
    l=[]
    for i in range(n):
        l.append(int(input()))
    print(duplicates(l))
if __name__ == "__main__":  
    main()