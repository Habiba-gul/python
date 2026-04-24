Emails={
    "abc@gmail.com",
    "xyz@gmail.com",
    "def@gmail.com",
    "abc@gmail.com",
}
print(Emails)

N=(1,1,2,3,4,5)
S=set(N)
print("unique",S)

s={1,2,3,5}
U={1,2,3,6,7}
s.add(4)
print("after add",S)

print(s|U)
print(s&U)