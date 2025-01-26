# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
#     print("Inner Loop", n)

# n = 5
# while n > 0:
#     print(n)
#     if n == 3:
#         break
#     n = n - 1

# Simple Login App
# while True:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
    
#     if username == "mike" and password == "0400":
#         print("Login Successful")
#         break
#     else:
#         print("Login Unsucessful")

# while True:
#     name = input("Enter your name: ")
#     if name == "mike":
#         continue
#     if name == "Mike":
#         break
#     print(name)

# For loops

# print(list(range(20)))

# for i in range(20):
#     print(i)
    
# for c in "Mike":
#     print(c)

# for i in range(20):
#     if i == 5:
#         break
#     print(i)  # prints 0 through 4
    
# for i in range(20):
#     if i == 5:
#         continue
#     print(i)  

# for i in range(4, 20): # prints even numbers
#     if i % 2 == 0:
#         print(i)  
        
        
# for i in range(4, 20): # prints odd numbers
#     if i % 2 != 0:
#         print(i) 
    
# for i in [1, 2, 3, 4, 5]:
#     print(i * i)

# names = ["Mike", "Bob", "Mary"]
# for name in names:
#     print(f"Welcome {name}!")
    
# nums = [1, 2, 3, 4, 5]
# print(sum(nums))
# print(max(nums))
# print(min(nums))
# print(len(nums))
# print(sum(nums) / len(nums))  # average

# nums = [1, 2, 3, 4, 5]

# total = 0
# count = 0

# for num in nums:
#     total = total + num
#     count = count + 1
# avg = total / count
# print(f"Total:{total} \nCount: {count} \nAverage: {avg}") 


# nums = [20, 0, -4, 100, 10000, 5, 70, 10]

# maximum = -1
# minimum = -1

# for i in nums:
#     if i > maximum:
#         maximum = i
#     if i < minimum:
#         minimum = i
# print("Maximum",maximum)
# print("Minimu",minimum)

# for  i in range(5):
#     if i > 3:
#         print(f"{i} greater than 3")

# minimum = None
# print("Before",minimum)
# for i in [20, 0, -4, 100, 10000, 5, 70, 10]:
#     if minimum is None:
#         minimum = i
#     elif i < minimum:
#         minimum = i
#     print(minimum, i)
    
        