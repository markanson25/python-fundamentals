'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
numbers_list = [5, 3, 4, 9, 2, 4, 7, 3, 5, 6, 1]

def sum1(list):
    total = 0
    for total in range(len(list)):
        total += total
    return print(total)

sum1(numbers_list)
