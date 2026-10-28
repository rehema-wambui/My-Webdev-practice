print("Good Morning Me")
print("Good Morning Me")
print("Good Morning Me")

def salutation(name, age):
    print(f"Good Morning {name} you are {age} years old")

salutation("ME", 22)
salutation("YOU", 30)
salutation("US", 52)

def add(a,b):
    sum = a + b
    return sum

print(add( 2, 4))
print(add(123, 234))

def areaCircle(radius, pi = 3.14):
    area = pi * radius **2
    return area
print(areaCircle(5))
print(areaCircle(20))
print(areaCircle(14))



def calculate_bmi():
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))
    if height_m <= 0 or weight_kg <= 0:
        print("Weight and height must be greater than zero.")
        return

    bmi = weight_kg / height_m ** 2
    if bmi < 18.5:
        weight_status = "Underweight"
    elif bmi < 25:
        weight_status = "Normal"
    elif bmi < 30:
        weight_status = "Overweight"
    else:
        weight_status = "Obese"

    print(f"BMI: {bmi:.2f} - {weight_status}")

calculate_bmi()


def area_of_circle(radius, pi = 3.14):
    if radius < 0:
        return "Radius cannot be negative"
    elif radius == 0:
        return "Area is zero"
    else:
        return pi * radius **2
print(area_of_circle(-1))
print(area_of_circle(0))
print(area_of_circle(14))

def divide_numbers(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    finally:
        print ("Division complete")
print(divide_numbers(20,0))
print(divide_numbers(20,4))

# create a function that takes users input in form of height and weight and calculates the BMI ,THEN LET it give out the response in regards to the BMI output (Overweight, Obese, Normal,Underweight)