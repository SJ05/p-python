# saving a variable
_greeting = "Hello World"
print(_greeting)

# asking the user to input something
greeting = input("Write a greeting: ")
print(greeting)

# simple operations using integers and floats
print("Simple operation")
z1 = 3
y1 = 5
x1 = z1+y1
print("3 + 5 = " + str(x1))
z2 = 2.5
y2 = 5.5
x2 = z2+y2
print("2.5 + 5.5 = " + str(x2))

# variables and operations
num = input("Enter any number: ")
int_num = int(num) + 15
print("Adding 15 using int() => " + str(int_num))
float_num = float(num) + 15
print("Adding 15 using float() => " + str(float_num))

"""
When doing multiple operations, exponents, division, multiplication
and so on is the order.
But if you use brackets, python will prioritize them from left to right
"""
operation = 10 - 5/5 * 1**2
print("Simple Operation: " + str(operation))
parentheses = (10-5) / (5*1) **2
print("With parentheses: " + str(parentheses))

# simple ops for strings
z = "Hello"
z.replace("H", "W")
# use dir() to see the functions you could do with strings
# use help() to see description about the function. (e.g) help("".replace)

# indexing and splitting
_greeting[0:2]
_greeting[:2]
_greeting[-3:-1]
_greeting[-3:]

# list, use the [] to get the object inside the list (e.g) s_list[0] will get "Syd"
s_list = ["Syd", 26, "ney"]
print(s_list[0])

# tupples, does not change
s_tupples = ("Syd", 26, "ney")

# dictionaries, has key pairs
s_dictionaries = {"Name": "Syd", "Age" : 26, "Likes" : ("Books", "Coding", "Eating")}



