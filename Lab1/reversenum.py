num=int(input("enter a number "))

orignal=num
reversed_num=0;
while num>0:
    last_dig=num%10;
    reversed_num=reversed_num*10+last_dig
    num=num//10

print("orignal number is",orignal)
print("reversed num is",reversed_num)

