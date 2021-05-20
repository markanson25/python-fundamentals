'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

starting_number = 0
user_secret_number = int(input("Please enter a number: "))
if 1000000000 < user_secret_number:
    user_secret_number = int(input("Please enter a different number: "))
while starting_number != user_secret_number:
    starting_number += 1
print(starting_number)
