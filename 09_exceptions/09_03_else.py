'''
Write a script that demonstrates a try/except/else.

'''

user_input = 0
message_to_user = "Welcome to the division calculator!  Enter two numbers and the calculator will give you the"\
                  " quotient.  Enter 'Exit' to quit the program."
print(message_to_user)
while user_input != "Exit":
    try:
        user_input = input("Please enter a number: ")
        dividend = int(user_input)
        user_input = input("Please enter a number: ")
        divisor = int(user_input)
        quotient = dividend/divisor
    except ValueError:
        print("Please only enter numbers.")
    except ZeroDivisionError:
        print("Okay, please enter a number that isn't zero: ")
    else:
        print(quotient)