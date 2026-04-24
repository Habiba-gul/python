def even(n):
    count=0
    for i in range(1,1+n):
      if i%2==0:
        print(i)
        count+=1

    return count

reslt=even(10)
print(reslt)