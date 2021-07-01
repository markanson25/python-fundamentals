'''
Demonstrate the use of the .enumerate() function.
'''

my_list = ["apple", "banana", "orange"]

new_list = [fruit for fruit in enumerate(my_list)]
print(new_list)
