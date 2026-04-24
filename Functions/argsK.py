# *args used for multiple args
def user_data(*num):
    total=0
    for n in num:
        total+=n
    return total

print(user_data(10,20,90,87))
