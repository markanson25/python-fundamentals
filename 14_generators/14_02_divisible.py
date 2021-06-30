'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

division_gen = (number for number in range(100000) if number % 1111 == 0)
for number in division_gen:
    print(number)
