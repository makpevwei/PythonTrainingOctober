# One way decision/multiple-if statement
# age = 18
# if age >= 18:
#     print("You are an adult.")
# if age > 17:
#     print("You can drive.")
# if age == 18:
#     print("You can vote.")
# if age < 18:
#     print("You cannot vote!")

# Comparison Operators
# Greater than: >
# Greater than or equal to: >=
# Less than: <
# Less than or equal to: <=
# Equal to: ==
# Not  equal to: !=

# num1 = 11
# num2 = 5

# print(num1 > num2)
# print(num1 >= num2)
# print(num1 < num2)
# print(num1 <= num2)
# print(num1 == num2)
# print(num1 != num2)

# Logical Operators
# and
# or
# not

# print(True and True and True) # True
# print(True and True and False) # False
# print(False and False and False) # False
# print(True or True or True) # True
# print(True or True or False) # True
# print(False or False or False) # False
# print(not True and not True) # False
# print(not True or not True) # False
# print(not True) # False
# print(not False) # True

# print((11 > 5) and (5 > 11)) #  False
# print((11 > 5) or (5 > 11)) # True


# Assignment Operators
# = 
# +=
# -=
# *=
# /=
# //=
# %=
# **=

# if-else statement
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
    
# Nested if-else statement
# age = int(input("Enter your age: "))
# country = input("Enter your country: ")


# if age >= 18 and country == "Nigeria":
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# if country == "Nigeria":
#     if age >= 18:
#         print("You are eligible to vote!")
#     else:
#         print("You are not eligible to vote!")
# else:
#     print("You are not from Nigeria.")

# Simple Login App
# username = input("Enter your username: ")
# password = input("Enter your passsword: ")

# if username ==  "mike" and password == "0400":
#     print("Login Successful!")
# else:
#     print("Login Unsuccessful!")

try:
    student_id = input("Enter your student id: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    gender = input("Enter your gender: ")
    mobile = input("Enter your mobile number: ")
    email = input("Enter your email address: ")
    exam_score = float(input("Enter your exam score: "))

    print()
    print("Student Grade App")
    print("-" * 16)
    print("Student ID:",student_id)
    print("First Name:",first_name)
    print("Last Name:",last_name)
    print("Gender:",gender)
    print("Mobile Number:",mobile)
    print("Email:",email)
    print("Exam Score:",exam_score)

    if exam_score >= 0 and exam_score < 40:
        print("Grade: F")
    elif exam_score >= 40 and exam_score < 45:
        print("Grade: E")
    elif exam_score >= 45 and exam_score < 50:
        print("Grade: D")
    elif exam_score >= 50 and exam_score < 60:
        print("Grade: C")
    elif exam_score >= 60 and exam_score < 70:
        print("Grade: B")
    elif exam_score >= 70 and exam_score <= 100:
        print("Grade: A")
    else:
        print("Invalid score") 
except ValueError as e:
    print("Error:",e)
    print("Invalid input. Please enter a numeric value.")

# try:
#     num1 = float(input("Enter a first number: "))
#     num2 = float(input("Enter a second number: "))
#     print(num1 / num2)
#     print(age)
# except Exception as e:
#     if  isinstance(e, ZeroDivisionError):
#         print("Error:",e)
#         print("Error: Division by zero is not allowed.")
#     elif isinstance(e,  ValueError):
#         print("Error:",e)
#         print("Error: Invalid input. Please enter a numeric value.")
#     else:
#         print("Error:",e)
#         print("Variable does nor exist.")  

# print(dir(__builtins__))

# print(isinstance(123, int))

    


