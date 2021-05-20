'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

# While loop

# total_amount = 0
# user_first_number = int(input("Please enter a number: "))
# user_second_number = int(input("Please enter a number: "))
# while user_first_number <= user_second_number:
#     accumulative_total = user_first_number + total_amount
#     total_amount = accumulative_total
#     user_first_number += 1
# print(accumulative_total)

# For Loop

total_amount = 0
user_first_number = int(input("Please enter a number: "))
user_second_number = int(input("Please enter a number: "))
for total in range(user_first_number, user_second_number + 1):
    cumulative = total + total_amount
    total_amount = cumulative
print(total_amount)
