'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

float_conversion = float(5)
print(float_conversion)

integer_conversion = int(1.0)
print(integer_conversion)

floor_division = 5000//3.7
print(floor_division)

first_number = float(input("Enter a number, any number: "))
second_number = float(input("Enter another number, any number: "))
result = first_number * second_number
print("The product is:", result)
