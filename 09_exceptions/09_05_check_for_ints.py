'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

class IntegerCheck(Exception):

    def check_for_integers(self, check_user_input):
        self.check_user_input = check_user_input
        self.user_input_type = type(user_input)
        return print(f"{self.user_input_type} isn't an integer, it's a {self.user_input_type}!")

user_input = input("Please enter an integer: ")
try:
    if type(user_input) == int:
        print("Good job!")
    else:
        raise ValueError
except ValueError:
    raise IntegerCheck(user_input)
