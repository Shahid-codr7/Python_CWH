def First2Last2(st):
    if(len(st)<2):
        return 'Empty String'
    return st[:2]+st[-2:]
def main():
    st=input("Enter sentence: ")
    print(First2Last2(st))
if __name__ == "__main__":
    main()