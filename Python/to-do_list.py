# Write a command-line to-do list application. The program should run in a loop, asking the user for a command (`add`, `view`, `quit`).
# add will ask for a task and add it to a list.
# view will print all the tasks.
# quit will exit the program.

tasks = []

while True:
    command = input("Enter a command (add, view, quit): ").lower()

    if command == "quit":
        print("Goodbye!")
        break
    elif command == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")
    elif command == "view":
        print("\nYour Tasks")
        if not tasks:
            print("You have no tasks.")
        else:
            # enumerate adds a counter to an iterable
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        print("_________________\n")
    else:
        print("Invalid command.")