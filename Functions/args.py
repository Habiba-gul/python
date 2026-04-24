# *args used for multiple args
def user_data(*num):
    total=0
    for n in num:
        total+=n
    return total

print(user_data(10,20,90,87))

# * stores args values in container then the container become tuple each value is access using for and operated 
