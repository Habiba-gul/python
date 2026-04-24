n=int(input("enter an number foe factorial :"))

factorial=1
for i in range(1,n+1):
    factorial=factorial*i

print(f"factorial of {n} is {factorial}")
