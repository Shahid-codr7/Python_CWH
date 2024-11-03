sent=input("Enter sentence: ")
s=sent.lower()
for vowel in s:
    if(vowel=='a' or vowel=="e" or vowel=="o" or vowel=="i" or vowel=="u"):
        l=sent.split(vowel)
        break
print(l)