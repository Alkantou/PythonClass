# range

list1 = list(range(0, 11))
print(list1)
baf = 'baf is bafi'
string1 = list("a s f")
print(string1)
print(baf.split())
print(list(baf))
print(list(range(0, 13, 2)))

# enumerate
# enumerate is a very useful function to use with for loops.

# Using for without enumerate.
index_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1
# Using enumerate function for the same situation.
for i, letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i, letter))
# enumerate is used to avoid using counts(?)
print(list(enumerate('Alexandros')))

# zip
# Creates a list of tuples by zipping up together two lists.
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
print(list(zip(mylist1, mylist2)))
for item1, item2 in zip(mylist1, mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1, item2))

# in operator
'x' in ['x', 'y', 'z']  # True
'x' in [1, 2, 3]  # False

# min and max
mylist = [10, 20, 30, 40, 100]
print(max(mylist), min(mylist))  # 100 10

# random library with some functions as example

from random import shuffle
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0, 41))

# input
x = input('Enter Something into this box: ')
print(str(x) + " is great")