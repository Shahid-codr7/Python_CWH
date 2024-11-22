def duplicates(l):
    ND=[]
    for i in range(10):
        if l[i] not in ND:
            ND.append(l[i])
    return ND
def main():
    print("Enter 10 nos. ")
    l=[]
    for i in range(10):
        l.append(int(input()))
    print(sorted(duplicates(l)))
if __name__ == "__main__":  
    main()