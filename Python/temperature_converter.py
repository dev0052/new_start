''' Create a program with two functions: celsius_to_fahrenheit and fahrenheit_to_celsius.
    Ask the user which conversion they want to perform and then calculate and print the result.
    Formulas: F=(Ctimes9/5)+32 and C=(F−32)times5/9. '''


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("\tConvert from Celsius or Fahrenheit?\n\tEnter (C) for Celsius or (F) for Fahrenheit\nEnter your choice: ").upper()
temp = float(input("Enter the temperature: "))

if choice == 'C':
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is {converted_temp:.2f}°F")
elif choice == 'F':
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is {converted_temp:.2f}°C")
else:
    print("Invalid choice.")