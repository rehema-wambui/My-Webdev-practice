class student:
    def __init__(self , name , age , course):
        self.name = name
        self.age = age
        self.course = course

    def introduce (self):
        print(f"My name is {self.name} and i am {self.age} years old pursuing {self.course}")

    def year_of_birth (self):
        return 2026 - self.age
    
student1 = student("Me",22, "IT")
student2 = student("You",27, "Law")

print(student1.course)
print(student2.name)
student1.introduce()
print(student1.year_of_birth())



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"{self.owner}'s balance: ksh{self.balance}")


account = BankAccount("Alex", 100)
print(account.owner)       # Access an attribute with dot notation
account.deposit(50)        # Call a method with dot notation
account.show_balance()

class Person:
    def __init__(self,name , gender , age):
        self.name = name
        self.gender = gender
        self.age = age
       
class Teacher(Person):
    def __int__(self, name, gender, age, sunject):
        super().self.__init__(name, gender, age)
        self.subject = sunject
Person1 =  Person("Her", "Female",20)
Teacher1 = Teacher("Him","Male",50)

# Encapuslation
class Mpesa:
    def __init__(self, name , balance):
        self.name = name
        self.__balance = balance
Mpesa1 = Mpesa("Him", 5000)
print(Mpesa1.balance)

# Abstraction
# polymrphism