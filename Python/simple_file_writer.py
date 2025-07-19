# Write a program that asks the user for a line of text and a filename, then writes that text to the specified file.


filename = input("Enter a filename (e.g., note.txt): ")
text_to_write = input("Enter the text to write to the file: ")

try:
    with open(filename, 'w') as file:
        file.write(text_to_write)
    print(f"Successfully wrote to {filename}")
except IOError:
    print(f"Error: Could not write to file {filename}.")