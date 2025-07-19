''' Write a program that takes a sentence and reverses the order of the words.
    For example, "Hello world this is Python" should become "Python is this world Hello".'''


sentence = input("Enter a sentence: ")

words = sentence.split() # Split the sentence into a list of words
words.reverse()          # Reverse the list in-place
reversed_sentence = " ".join(words) # Join the list back into a string

print(reversed_sentence)
