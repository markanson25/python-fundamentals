'''

Write a script that completes the following tasks.

'''

# take in a number from the user between 1 and 1,000,000,000
user_input = int(input("Please enter a number between 1 and 1,000,000,000: "))
if user_input < 0 or user_input > 1000000000:
    user_input = int(input("Please enter a number between 1 and 1,000,000,000: "))
else:
# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
    def single_divisor(number):
        either_divisor = False
        four_divisor_math = number % 4
        seven_divisor_math = number % 7
        if four_divisor_math == 0 or seven_divisor_math == 0:
            either_divisor = True
        return either_divisor

    # define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
    def both_devisor(number):
        bothum_devisor = False
        four_divisor_math = number % 4
        seven_divisor_math = number % 7
        if four_divisor_math == 0 and seven_divisor_math == 0:
            bothum_devisor = True
        return bothum_devisor

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
    single_divisor_result = single_divisor(user_input)
    both_devisor_result = both_devisor(user_input)
# print your new variables to display the results
    print(f"Whether the number you entered can be divided by either 4 or 7 evaluated to: {single_divisor_result}.")
    print(f"Whether the number you entered can be divided by both 4 and 7 evaluated to: {both_devisor_result}.")

