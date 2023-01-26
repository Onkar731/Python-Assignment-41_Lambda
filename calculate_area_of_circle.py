"""
Write a lambda expression to calculate area of a circle
"""

# taking input from the user
radius = float(input("Enter radius of the circle : "))

# calculating area of a circle
print("Area of the circle :",(lambda radius: 3.14*radius*radius)(radius))
