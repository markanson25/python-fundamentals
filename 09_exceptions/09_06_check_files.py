'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
import random
with open("integers.txt", "r") as integers_text:
    first_line = integers_text.readline()
    first_line_stripped = first_line.strip()
    try:
        first_line_int = int(first_line_stripped)
    except IOError:
        print("We encountered an IOError!")
    except ValueError:
        print("We encountered a ValueError!")
    else:
        lets_multiply = first_line_int * random.randint(2, 999999999)
        print(lets_multiply)
