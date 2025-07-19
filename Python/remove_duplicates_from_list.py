# Write a program that takes a list with duplicate values and returns a new list with only the unique values.


my_list = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]

unique_list = list(set(my_list))

print(f"Original List: {my_list}")
print(f"Unique List: {unique_list}")