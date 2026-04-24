# ArmStrong

# enter a 3-digit number
number=int(input("enter a 3 digit number"))

if number<100 and number>999:
    print("enter valid 3-digit number")
else:
    hundered=number//100 #first digit
    tens=(number//10)%10  #second digit
    ones=number%10    # third digit

sum_of_cube=(hundered**3)+(tens**3)+(ones**3)

if sum_of_cube==number:
    print("armstrong")
else:
    print("no armstrong")