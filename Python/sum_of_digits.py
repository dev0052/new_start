''' Write a program that calculates the sum of the digits of a number entered by the user.
    For example, if the input is 123, the output should be 1 + 2 + 3 = 6'''


num_str = input("Enter a number: ")
digit_sum = 0

for digit in num_str:
    if digit.isdigit():
        digit_sum += int(digit)

print(f"The sum of the digits is: {digit_sum}")