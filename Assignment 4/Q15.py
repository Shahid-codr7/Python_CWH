word=input('Enter: ')
vowel='aeiouAEIOU'
if(word[0] in vowel):
    word+='way'
else:
    for i in range(len(word)):
        if(word[i] not in vowel):
            word=word[i+1:]+word[i]+'ay'
            break
print(word.lower())