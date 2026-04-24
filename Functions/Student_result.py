def StudentResult(marks):
    if marks>=40:
        return("pass")
    else:
        return("fail")

# result=StudentResult(60)
# print(result)  
marks = int(input("enter your marks"))

result=StudentResult(marks)

print(result)
        