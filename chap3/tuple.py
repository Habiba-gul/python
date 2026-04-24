days=("mon","tue","wed")
# print(days)

# days[0]="fri"  not possible
print(days)

x=(10,)
print(type(x))

y=(1,2,3,4,5)
# print(y[-1])
for i in y:
    print(i)

print(len(y))

# also used to count freq of a num
z=(10,10,60,60,60,30,90,30)
print(z.count(60))

# to find index of a value
print(z.index(90))
