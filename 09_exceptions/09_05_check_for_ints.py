'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

integer_check = False
while integer_check == False:
    try:
        user_input = input("Please enter an integer: ")
        user_input_int = int(user_input)
        user_input_float = float(user_input)
        if user_input_float % user_input_int != 0:
            raise ValueError
        else:
            print("Good job!")
            integer_check = True

    except:
        print("Sorry, that was not an integer.")


