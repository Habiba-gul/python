
char=input("enter a character:").lower()

if char in 'aeiou':
    print("its a vowel")
elif char.isalpha():
    print("its a consonent")
else:
    print("not a character")