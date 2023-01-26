"""
Write a lambda expression to check if a number is even
"""

# to define a lambda expression we must write lambda keyword before the expression
# Syntax - lambda input:expression
# lambda expression is prefered to write single line function
# Lambda expression is anonymous function which is define where we want to call it

# taking input from the user
num = int(input("Enter a number : "))

# checking whether the number is even or not
print((lambda num: "Even" if num%2 == 0 else "Not Even")(num))