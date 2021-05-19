'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5

user_number = int(input("Please enter a number: "))
starting_number = 1
while user_number >= starting_number:
    star_output = "*" * starting_number
    print(star_output)
    starting_number += 1

