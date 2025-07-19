# Write a program that counts the number of vowels and consonants in a string provided by the user. The count should be case-insensitive.

vowels = "aeiou"
user_string = input("Enter a string: ").lower()

vowel_count = 0
consonant_count = 0

for char in user_string:
    if char.isalpha(): # Check if the character is an alphabet letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")