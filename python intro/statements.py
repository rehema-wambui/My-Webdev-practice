age = 20
if age > 18:
    print("You are an adult")
else:
    print("You are a child")

marks = 0
if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:  
    marks <= 40
    print("Grade E")
# create a simple BMI system using conditional statements let weight and height be users inputs
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.1f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
