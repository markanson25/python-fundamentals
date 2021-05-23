'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''

print_number_count = 1
number_string = ''
number_count = 0
while number_count < 50:
    number_string += str(number_count) + " "
    if print_number_count == 10:
        print(number_string)
        print_number_count = 0
        number_string = ''
    number_count += 1
    print_number_count += 1
