import sys

def get_user_input():
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        return weight, height
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_user_input()

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def display_result(bmi, category):
    print(f"Your BMI is {bmi:.2f} and you are classified as {category}.")

def main():
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    display_result(bmi, category)

if __name__ == "__main__":
    main()
