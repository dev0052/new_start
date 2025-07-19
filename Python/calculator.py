while True:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    action = input("Please select the operation you want to perform:- \n\tEnter 1 to perform addition\n\tEnter 2 to perform subtraction\n\tEnter 3 to perform multiplication\n\tEnter 4 to perform division\n\tEnter 0 to exit\n")

    if action == "1":
        print(f"The result of addition is: {a + b}")
    elif action == "2":
        print(f"The result of subtraction is: {a - b}")
    elif action == "3":
        print(f"The result of multiplication is: {a * b}")
    elif action == "4":
        if b != 0:
            print(f"The result of division is: {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    elif action == "0":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid selection. Please enter a number between 0 and 4.")
