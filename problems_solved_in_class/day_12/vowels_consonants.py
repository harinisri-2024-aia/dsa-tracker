str=input()
vowels=0
consonants=0
vowelsset="aeiouAEIOU"
for ch in str:
    if ch.isalpha():
        if ch in vowelsset:
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)