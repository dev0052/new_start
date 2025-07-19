# Write a program that reads a text file and counts the number of words in it.


filename = input("Enter the filename to read from: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"The file '{filename}' contains {word_count} words.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    print(f"Error: Could not read the file.")