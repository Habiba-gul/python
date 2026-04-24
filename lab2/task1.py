#map() is used to convert each element of a list into another type.

# Taking input for first list
list1 = list(map(int, input("Enter elements of list 1 (space separated): ").split()))

# Taking input for second list
list2 = list(map(int, input("Enter elements of list 2 (space separated): ").split()))

# Merging lists
merged_list = list1 + list2

# Sorting merged list
merged_list.sort()

# Display result
print("Sorted merged list:", merged_list)