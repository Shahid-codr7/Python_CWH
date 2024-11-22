word=input("Enter word: ")
v='aeiouAEIOU'
for i in word:
    if i in v:
        print(word.split(i))
        break
