Name = input("Enter your name : " )
Age = int(input("Enter your Age : "))
Height = float(int("Enter your Height "))
is_student = bool(input("please confirm your a student True/Flase : "))

# Print all values in a single print statement
print(name, age, height, is_student)

# Task 2: String Formatting
print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")

# Task 3: Arithmetic Operations
age_in_months = age * 12
age_in_days = age * 365
remainder = age % 7
age_square = age ** 2

print("Age in months:", age_in_months)
print("Age in days:", age_in_days)
print("Remainder when age is divided by 7:", remainder)
print("Age squared:", age_square)