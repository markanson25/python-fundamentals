'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

mylist = []
mytuple = ()
user_input = input("Please enter a sentence: ")
print(split_user_input)
for letter in user_input:
    mytuple = (letter,)
    mylist.append(mytuple)
print(mylist)

