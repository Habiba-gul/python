n=int(input("how many number you want to enter:"))

even_sum=0

odd_sum=0

for i in range(n):
    num=int(input(f"enter the number {i+1} :"))
    if num%2==0:
        even_sum=even_sum+num
    else:
        odd_sum=odd_sum+num

print("sum of even number",even_sum)
print("sum of odd number",odd_sum)
        