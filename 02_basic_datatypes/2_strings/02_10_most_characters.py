'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

sentence_a = input("Please enter a sentence: ")
sentence_b = input("Please enter a second sentence: ")
sentence_c = input("Please enter a third sentence: ")
sentence_a_length = len(sentence_a)
sentence_b_length = len(sentence_b)
sentence_c_length = len(sentence_c)
print(sentence_a_length, ", ", sentence_a)
print(sentence_b_length, ", ", sentence_b)
print(sentence_c_length, ", ", sentence_c)
if sentence_b_length < sentence_a_length > sentence_c_length:
    print("Your first sentence was the longest at", sentence_a_length, "letters.")
elif sentence_a_length < sentence_b_length > sentence_c_length:
    print("Your second sentence was the longest at", sentence_b_length, "letters.")
else:
    print("Your third sentence was the longest at", sentence_c_length, "letters.")

