'''Write a program that counts the frequency of each character in a string.
Store the results in a dictionary.
For "hello", the output should be something like {'h': 1, 'e': 1, 'l': 2, 'o': 1}'''


user_string = input("Enter a string: ")
frequency = {}

for char in user_string:
    # .get(key, default) is a safe way to get a key's value
    # If the key doesn't exist, it returns the default (0 in this case)
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:")
print(frequency)