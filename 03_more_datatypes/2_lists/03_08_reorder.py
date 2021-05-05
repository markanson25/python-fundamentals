'''
Read in 10 numbers from the user. Place all 10 numbers into a list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

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
mylist = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
print(mylist)
mylist[0] = num2
mylist[1] = num4
mylist[2] = num6
mylist[3] = num8
mylist[4] = num10
mylist[5] = num9
mylist[6] = num7
mylist[7] = num5
mylist[8] = num3
mylist[9] = num1  # 2,4,6,8,10,9,7,5,3,1
print(mylist)
