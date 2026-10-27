# user input
name = "Ishmael"
print(name)

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
age = input("Enter your age: ")
print(f"{first_name} {last_name} your age is {age}")

num1 = int( input("Enter your first number: "))
num2 =  int(input("Enter your second number: "))
total = num1 + num2
print(total)

price = float(input("Enter the price: "))
Quantity = float(input("Enter the quality: "))
total_amount = price * Quantity
print(f"Total cost is Ksh {total_amount}")

# ask the user for amount paid and calculate the change due assuming amount paid is sufficient
amount_paid = float(input("Enter the amount paid: "))
change_due = amount_paid - total_amount
print(f"Change due is Ksh {change_due}")
