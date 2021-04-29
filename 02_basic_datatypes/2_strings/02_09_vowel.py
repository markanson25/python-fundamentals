'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

sentence = input("Please enter a sentence: ")
vowel1 = "a"
vowel2 = "e"
vowel3 = "i"
vowel4 = "o"
vowel5 = "u"
result = sentence.count(vowel1) + sentence.count(vowel2) + sentence.count(vowel3) + sentence.count(vowel4) + sentence.count(vowel5)
result_a = sentence.count(vowel1)
result_b = sentence.count(vowel2)
result_c = sentence.count(vowel3)
result_d = sentence.count(vowel4)
result_e = sentence.count(vowel5)
print("There is a total of", result, "vowels in your string.")
print("There is a total of", result_a, "'a' vowels in your string.")
print("There is a total of", result_b, "'e' vowels in your string.")
print("There is a total of", result_c, "'i' vowels in your string.")
print("There is a total of", result_d, "'o' vowels in your string.")
print("There is a total of", result_e, "'u' vowels in your string.")
