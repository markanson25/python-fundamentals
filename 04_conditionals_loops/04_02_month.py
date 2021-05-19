'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

user_month_input = int(input("Please enter a number that corresponds to a month: "))
if user_month_input == 1:
    print("January")
elif user_month_input == 2:
    print("February")
elif user_month_input == 3:
    print("March")
elif user_month_input == 4:
    print("April")
elif user_month_input == 5:
    print("May")
elif user_month_input == 6:
    print("June")
elif user_month_input == 7:
    print("July")
elif user_month_input == 8:
    print("August")
elif user_month_input == 9:
    print("September")
elif user_month_input == 10:
    print("October")
elif user_month_input == 11:
    print("November")
elif user_month_input == 12:
    print("December")
else:
    print("Other")
