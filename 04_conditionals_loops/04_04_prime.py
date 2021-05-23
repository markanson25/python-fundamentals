'''
Print out every prime number between 1 and 100.

'''
prime_numbers_list = []
for prime_numbers in range(2, 100):
    starter = 2
    even_division_found = False
    while starter < prime_numbers:
        remainder_division = prime_numbers % starter
        if remainder_division == 0:
            even_division_found = True
        starter += 1
    if even_division_found == False:
        prime_numbers_list.append(prime_numbers)
print(prime_numbers_list)
