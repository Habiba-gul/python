S=input("enter any words or letters:")
vowels="aeiouAEIOU"
vowel_count=0
for char in S:
    if char in vowels:
        vowel_count+=1

print(vowel_count)