word=input('Enter: ')
word=word.lower()
vowel=['a','e','i','o','u']
if(word[0] in vowel):
    word+='way'
else:
    for i in range(len(word)):
        if(word[i] not in vowel):
            word=word[i+1:]+word[i]+'ay'
            break
print(word)