# reverse digits of a number
N=int(input("enter a number :"))
# check for negative num
if N<0:
    is_negative=True
    N=abs(N)
else:
    is_negative=False
    reversed_str=""
    # convert int to str
str_num=str(N)

for digit in str_num:
    reversed_str=digit + reversed_str

reversed_num=int(reversed_str)

if is_negative:
    reversed_num=-reversed_num
print(reversed_num)
