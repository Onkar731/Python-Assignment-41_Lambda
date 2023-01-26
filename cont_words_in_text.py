"""
Write a lambda expression to count words in a given text
"""

# taking input from the user
string = input("Enter a string : ")

# counting words in a given text
print("Total number of words in given text :",(lambda string: len(string.split(' ')))(string))