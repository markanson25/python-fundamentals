'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

value1 = input("Please enter a value: ")
value2 = input("Please enter a value: ")
value3 = input("Please enter a value: ")
value4 = input("Please enter a value: ")
value5 = value2
value6 = value4
thelist = [value1, value2, value3, value4, value5, value6]
print(thelist)
countedvalue1 = thelist.count(thelist[0])
if countedvalue1 > 1:
    thelist.remove(value1)
countedvalue2 = thelist.count(thelist[1])
if countedvalue2 > 1:
    thelist.remove(value2)
countedvalue3 = thelist.count(thelist[2])
if countedvalue3 > 1:
    thelist.remove(value3)
countedvalue4 = thelist.count(thelist[3])
if countedvalue4 > 1:
    thelist.remove(value4)
countedvalue5 = thelist.count(thelist[4])
if countedvalue5 > 1:
    thelist.remove(value5)
countedvalue6 = thelist.count(thelist[5])
if countedvalue6 > 1:
    thelist.remove(value6)
print(thelist)
