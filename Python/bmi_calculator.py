'''Write a program that calculates the Body Mass Index (BMI) from a user's weight (in kg) and height (in meters).
After calculating, classify the BMI into categories (e.g., Underweight < 18.5, Normal 18.5-24.9, etc.).
The formula is BMI = weight / (height * height)'''


def calculate_bmi(weight, height):
    if height <= 0:
        return None
    return weight / (height * height)

def classify_bmi(bmi):
    if bmi is None:
        return "Invalid height."
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

try:
    weight_kg = float(input("Enter your weight in kg: "))
    height_m = float(input("Enter your height in meters: "))

    bmi_value = calculate_bmi(weight_kg, height_m)
    category = classify_bmi(bmi_value)

    if bmi_value is not None:
        print(f"Your BMI is: {bmi_value:.2f}")
        # .2f formats to 2 decimal places
    print(f"Category: {category}")

except ValueError:
    print("Invalid input. Please enter numbers only.")