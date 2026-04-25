# encapsulation hide  data from 3rd party 
# private var ----- (double underscore) __private


# when there is no encap any one can change the user info


# class bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance


# acc=bankaccount("habiba",20000)
# # changed balance no sec
# acc.balance=1000
# print(acc.name)
# print(acc.balance)

# to avoid such senerio we use 

class bankacc:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance   #private var 
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def withdraw(self,amount):
        if 0< amount<= self.__balance:
              self.__balance-=amount
        else:
            print("invalid amount")

    def get__balance(self):
        return self.__balance
    
acc= bankacc("habiba",10000)
print("before deposit and with draw balance",acc.get__balance())
acc.deposit(5000)
print("balance after deposit:", acc.get__balance())
acc.withdraw(2000)
print("balance after withdraw:",acc.get__balance())
    
        

          
    




        
        


