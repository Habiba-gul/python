#user input list with 10-12 iteams
# targested element
# search 1 by 1 element
# indexing number
list_iteam=list(input("enter values of iteam in list :"))

targeted_value=input("enter targeted value in the list :")

found=False

for i in range(len(list_iteam)):
    if list_iteam[i]==targeted_value:
        print("iteam is found at index:",i)
        found=True
    else:
       print("not found")

