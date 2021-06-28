'''

Write a script that removes all duplicates from a list.

'''

mylist = [1, 2, 3, 4, 3, 4, 5]
for element in mylist:
    counted_number = mylist.count(element)
    if counted_number > 1:
        mylist.remove(element)
print(mylist)



