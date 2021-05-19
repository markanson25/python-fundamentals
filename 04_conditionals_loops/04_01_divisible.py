'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

user_number = int(input("Please enter a number: "))
if user_number > 1000000000:
    user_reply_big = int(input("Please enter a smaller number: "))
    user_number = user_reply_big
elif user_number < 1:
    user_reply_small = int(input("Please enter a larger number: "))
    user_number = user_reply_small
user_number_division_check = user_number % 3
user_number_division = int(user_number / 3)
if user_number_division_check == 0:
    print(user_number, "is divisable by 3!", "The result is:", user_number_division)
else:
    print(user_number, "is not divisable by 3.")

