'''
Write a script with a function that demonstrates the use of *args.

'''

def addition(*args):
    old_number = 0
    for number in args:
        add_input = number + old_number
        old_number += number
        print(f"Your answer is: {add_input}")

addition(2, 4, 1, 3)