'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

del list_[2]
list_.remove(4)
list_.sort()
print(list_)

