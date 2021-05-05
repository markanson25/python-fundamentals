'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))
num4 = int(input("Please enter a number: "))
num5 = int(input("Please enter a number: "))
num6 = int(input("Please enter a number: "))
num7 = int(input("Please enter a number: "))
num8 = int(input("Please enter a number: "))
num9 = int(input("Please enter a number: "))
num10 = int(input("Please enter a number: "))
thelist = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
for x in thelist:
    total = sum(thelist)
print(thelist)
print(total)

