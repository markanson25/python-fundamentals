'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

output_list = []
user_input_list = []
while len(user_input_list) < 7:
    user_input = int(input("Please enter a number: "))
    user_input_list.append(user_input)
user_input_list.sort()
print(user_input_list)
for number_pairs in range(1, len(user_input_list), 2):
    if number_pairs < 2:
        print(number_pairs)
        odd_number_input = [number_pairs, 0]
        print(odd_number_input)
        odd_number_input = number_pairs
        print(number_pairs)
        user_input_list.append(number_pairs)
        print(user_input_list)
    tup = (user_input_list[number_pairs], user_input_list[number_pairs + 1])
    output_list.append(tup)
print(output_list)


