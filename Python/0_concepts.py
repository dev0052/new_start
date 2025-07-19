# # taking input from the user
# name = input("Enter your name: ");
# # printing input
# print(f"Hello, {name}");


# # variables and type casting
# age = input("Enter your age: ")
# # by default the input will be stored as a string if we need to convert it we will use typecasting
# age_int = int(age)
# # we can confirm by printing type of variables
# print("type of age is : ",type(age))
# print("type of age_int is : ",type(age_int))


# # Controlled flow
# # lets your code make decisions
# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif 18 <= age < 50:
#     print("You are an adult.")
# else:
#     print("You are a senior.")


# # loops , repeating actions
# # for loop
# # Loop through a list
# for task in ["laundry", "dishes"]:
#     print(f"To do: {task}")
# # Loop 5 times (from 0 to 4)
# for i in range(5):
#     print(i)
# # while loop
# command = ""
# while command != "quit":
#     command = input("Enter a command: ")
# # break , Immediately exits the current loop


# # Data Structures, Storing Collections
# # Lists []
# list_a = [111 , "string" , 13.7]
# list_a.append("new item") #add item to end of the list
# print(list_a[3]) #print a element
# # Dictionaries {}
# person = {"name": "Jane", "age": 28}
# person["city"] = "London"            # Add/update a key-value pair
# print(person["name"])                # Access by key -> "Jane"
# print(person.get("job", "Unemployed")) # Safely get a key, with a default
# # Sets set()
# numbers = [1, 2, 2, 3, 3, 3]
# unique_numbers = list(set(numbers)) # -> [1, 2, 3]
# print(unique_numbers)


# # Functions
# def addition(a, b):
#     result = a + b
#     return result
# # Call the function
# c = addition(5, 10)
# print(c)


# # Error and file handling
# # try-except
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("That wasn't a valid number!")
# # with open
# # Writing to a file ('w' mode overwrites the file)
# with open("note.txt", "w") as file:
#     file.write("Hello, world!")
# Reading from a file ('r' mode)
# with open("note.txt", "r") as file:
#     content = file.read()
