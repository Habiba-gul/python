# Birthday dictionary
birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")

# Display names
for name in birthdays:
    print(name)

# Ask user
person = input("Who's birthday do you want to look up? ")

# Display result
if person in birthdays:
    print(person + "'s birthday is " + birthdays[person])
else:
    print("Sorry, we don't have that person's birthday.")