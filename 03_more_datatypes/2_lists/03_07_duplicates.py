'''

Write a script that removes all duplicates from a list.

'''

mylist = [1, 2, 3, 4, 3, 4, 5]
for number in mylist:
    counted_number = mylist.count(number)
    if counted_number > 1:
        mylist.remove(number)
print(mylist)



