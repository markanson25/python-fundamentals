'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

division_gen = (number//1111 for number in range(100000) if number % 1111 == 0)
for number in division_gen:
    print(number)
