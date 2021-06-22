'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''

x = "This is a string."
try:
    y = int(x)
except NameError as define_variables:
    print("Maybe you should define your variables first")
except ValueError as wrong_data_type_conversion:
    print("You cannot convert a string into an integer.")
else:
    print(y)

