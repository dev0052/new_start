'''Write a program to find the largest number in a list of numbers without using the built-in max() function.'''


numbers = [12, 4, 56, 99, 13, 8]

if not numbers:
    print("The list is empty.")
else:
    largest_so_far = numbers[0]
    for num in numbers:
        if num > largest_so_far:
            largest_so_far = num
    print(f"The largest number is: {largest_so_far}")