# Taking input for first list
list1 = list(map(int, input("Enter elements of list 1 (space separated): ").split()))

# Taking input for second list
list2 = list(map(int, input("Enter elements of list 2 (space separated): ").split()))

# Merging lists
merged_list = list1 + list2

# Sorting merged list
merged_list.sort()

# Finding smallest and largest
smallest = min(merged_list)
largest = max(merged_list)

# Display result
print("Sorted merged list:", merged_list)
print("Smallest element:", smallest)
print("Largest element:", largest)