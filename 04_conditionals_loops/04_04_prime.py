'''
Print out every prime number between 1 and 100.

'''
prime_numbers_list = []
starter = 2
for prime_numbers in range(2, 100):
    while starter <= 100:
        remainder_division = prime_numbers % starter
        whole_number_division = prime_numbers / starter
        if prime_numbers != starter:
            if remainder_division == 0 and whole_number_division < 2:
                prime_numbers_list.append(prime_numbers)
        starter += 1
        if starter == 100:
            starter = 2
            break
print(prime_numbers_list)
