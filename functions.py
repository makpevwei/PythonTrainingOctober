### Default argument
### Pass Statement
### Keyword arguments (named arguments)
### Positional arguments
### functions without parameters
### functions with one
### functions that return a value
### functions with multiple arguments and multiple return values using tuples
### lambda functions - Lambda functions are similar to user-defined functions but without a name. 
### They're commonly referred to as anonymous functions.
### Docstrings - describes what your fuction does. It serves as a documentation to your function. Placed in the immediate line after the function header.
### Arbitrary positional arguments (*args)
### Arbitrary keyword arguments (**kwargs)
### Ternary operator determines if a condition is true or false and then returns the appropriate value in accordance with the result.
### The ternary operator is useful in cases where we need to assign a value to a variable based on a simple condition, and we want to keep our code more concise — all in just one line of code
### global and local scope, the global keyword
### Assert keyword
### The global keyword is used to create global variables from a no-global scope, e.g. inside a function.

# def greeting(): # Defining or creating the function
#     print("Welcome Mike!")
    

# greeting() # Invoking or calling the function

# A parameter is a variable created inside the parathessis of a function.
# We can have single or multiple parameters.
# An argument is the value we replace the parameter with when we call the function.

# def greeting(name): # name is a parameter
#     print(f"Welcome {name}!")
    

# greeting("Mike") # Invoking or calling the function

# def greeting(name, age, gender): # name, age and gender are parameters
#     print(f"Welcome {name}, you are {age} years old and you are a {gender}!")
    

# greeting("Mike", 30, "Male") # Invoking or calling the function

# def greeting(): 
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     gender = input("Enter your gender: ")
#     print(f"Welcome {name}, you are {age} years old and you are a {gender}!")
    

# greeting() # Invoking or calling the function

# def greeting(name, age, gender): 
#     print(f"Welcome {name}, you are {age} years old and you are a {gender}!")
    
# greeting("Mike", 30, "Male") # Positional Argument


# def greeting(name, age, gender="Male"): 
#     print(f"Welcome {name}, you are {age} years old and you are a {gender}!")
    
# greeting("Mike", 30) # Default Argument


# def greeting(name, age, gender): 
#     print(f"Welcome {name}, you are {age} years old and you are a {gender}!")
    
# greeting(age=30, name="Mike", gender="Male") # keyword Argument

# def greeting(): 
#     pass

# def greeting(): 
#     return "Hello Mike!"

# greet = greeting()
# print(greet)


# def greeting(name, age, gender): 
#     return f"Welcome {name}, you are {age} years old and you are a {gender}!"
    
# print(greeting(age=30, name="Mike", gender="Male"))


# def greeting(name, age, gender): 
#     return name, age, gender
    
# print(greeting(age=30, name="Mike", gender="Male"))

# def add_num(a, b):
#     return a + b

# total = add_num(3, 5)
# print(total) # Output: 8

# total = add_num(11, 5)
# print(total)

# total = lambda a, b, c: a + b + c
# print(total(11, 5, 4))

# greeting = lambda name:  f"Hello {name}!"
# print(greeting("Mike"))

# print(print.__doc__)
# help(print)
# print("Mike", 30); print("Bob", 40)


# def greeting(name, age, gender): 
#     """
#     This function returns a greeting message to the user.
#     """
#     return f"Welcome {name}, you are {age} years old and you are a {gender}!"
    
# print(greeting(age=30, name="Mike", gender="Male"))

# print(greeting.__doc__)
# print(help(greeting))

# Tenary Operator
# age = int(input("Enter your age: "))
# print("You are eligible to vote") if age >= 18 else  print("You are not eligible to vote")


# def greeting(): # name, age and gender is local to the function 
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     gender = input("Enter your gender: ")
#     print(f"Welcome {name}, you are {age} years old and you are a {gender}!")
    
# greeting()


# def greeting(): 
#     global name, age, gender
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     gender = input("Enter your gender: ")
#     print(f"Welcome {name}, you are {age} years old and you are a {gender}!")

# greeting()

# print(name, age, gender)


# name = "Mike"
# def greeting():   
#     # name = input("Enter your name: ")
#     return f"Welcome  {name}!"

# print(greeting())  

# def add_nums(a, b):
#     return a + b

# print(add_nums(3, 3))

# # Arbitary positional arguments (args)
# def  add_nums(*args):
#     print(type(args))
#     return sum(args)

# print(add_nums(*[1,2,3,4,5]))
# print(add_nums(*(1,2,3,4,5)))

# Arbitary keyword arguments (kwargs)
# def add_nums(**kwargs):
#     print(type(kwargs))
#     result = kwargs["one"] + kwargs["two"]
#     return result

# print(add_nums(**{"one":1,"two":2}))

      