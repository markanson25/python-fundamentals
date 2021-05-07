'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

#  Thank you Michael!!!

user_inputs = []
max_number = -1000
while len(user_inputs) < 10:
    user_input = int(input("Please enter a number: "))
    user_inputs.append(user_input)
    if user_input > max_number:
        max_number = user_input
total = sum(user_inputs)
print("The largest number in the list is:", max_number)
print("The sum of the list is: ", total)

