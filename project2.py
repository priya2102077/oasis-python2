def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI).

    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: BMI value
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify the BMI value into categories.

    :param bmi: BMI value
    :return: Category as a string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """
    Main function to run the BMI calculator.
    """
    print("Welcome to the BMI Calculator")

    # Prompt the user for weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify BMI
        category = classify_bmi(bmi)

        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
