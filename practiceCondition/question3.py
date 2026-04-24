num=int(input("enter a number :"))

if num% 3==0 and num%5== 0:
    print("number is divisble by both 3 and 5")
elif num%5==0:
    print("number is divisble by 5")
elif num%3==0:
    print("number is divisble by 3")
else:
    print("number is not divisble by both 3 and 5")