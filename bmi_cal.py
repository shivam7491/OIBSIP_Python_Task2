import csv
import os


def calculate_bmi(weight, height, is_metric):
    if height <= 0:
        raise ValueError("Height must be positive.")

    if is_metric:
        bmi = weight / (height / 100) ** 2  # Convert cm to m
    else:
        bmi = (weight * 703) / (height ** 2)  # Imperial calculation

    return bmi


def classify_bmi(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi <= 25:
        return "Normal"
    elif 25 < bmi <= 30:
        return "Overweight"
    else:
        return "Obese"


def store_bmi_data(weight, height, bmi, category, scale):
    DATA_FILE = "bmi_data.csv"

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Weight", "Height", "BMI", "Category", "Scale"])

    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([weight, height, bmi, category, scale])


def load_bmi_data():
    DATA_FILE = "bmi_data.csv"

    if not os.path.exists(DATA_FILE):
        return []  # Return empty list if no file

    with open(DATA_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        return data 


def main():
    while True:
        try:
            scale = input("Choose measurement scale (metric/imperial): ").lower()
            if scale not in ('metric', 'imperial'):
                raise ValueError("Invalid scale. Choose 'metric' or 'imperial'")

            if scale == 'metric':
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (cm): "))
            else:
                weight = float(input("Enter weight (pounds): "))
                height = float(input("Enter height (inches): "))

            bmi = calculate_bmi(weight, height, scale == 'metric')
            category = classify_bmi(bmi)
            print(f"BMI: {bmi:.1f} ({category})")

            store_data = input("Store this data? (y/n): ").lower()
            if store_data == 'y':
                store_bmi_data(weight, height, bmi, category, scale)

            continue_check = input("Continue checking BMI? (y/n): ").lower()
            if continue_check != 'y':
                break  # Exit the loop

        except ValueError as e:
            print(f"Invalid input: {e}") 

if __name__ == "__main__":
    main()
