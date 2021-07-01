'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

my_iterable_list = ['one', 'two', 'three', 'four']

def my_enumerate(iterable):
    index = 0
    return_list = []
    for iteration in iterable:
        create_tuple = (index, iteration)
        return_list.append(create_tuple)
        index += 1
    return return_list

print(my_enumerate(my_iterable_list))