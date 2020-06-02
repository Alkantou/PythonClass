my_list1 = [4, 8, 13, 17, 28]
my_list2 = ['Alexandros', 33, 3.14, 'g']
print(len(my_list1), len(my_list2))  # Prints: 5 4
# Indexing and Slicing
print(my_list2[0] + str(my_list1[2]))  # Prints Alexandros13
print(my_list2[:3:2])  # Prints ['Alexandros', 3.14]
# add items to lists but NOT change the original list
print(my_list2 + ['Vafouskos', 'Elena'])
# BUT you can reassign your list
my_list2 = my_list2 + ['Vafouskos', 'Elena']
print(len(my_list1), len(my_list2))  # Prints 5 6
print(my_list2*2)  # ['Alexandros', 33, 3.14, 'g', 'Vafouskos', 'Elena',
# 'Alexandros', 33, 3.14, 'g', 'Vafouskos', 'Elena'] But NOT permanent

# Basic List Methods

my_list1.append("nanaNanana")
print(my_list1)  # [4, 8, 13, 17, 28, 'nanaNanana']
my_list1.pop()   # pops by default the last object of the list but we can assign any index
print(my_list1)  # [4, 8, 13, 17, 28]
print(my_list1.pop())
print(my_list1)

# Method .reverse()
my_list2.reverse()
print(my_list2)  # ['Elena', 'Vafouskos', 'g', 3.14, 33, 'Alexandros']  Permanent
# Method .sort()
my_list3 = ['b', 'v', 'g', 'a', 'g', 'h', 'h', 'r', 'w', 'y']
my_list4 = [5.3, 55, 8, 15, 2, 14, 233, 49]
my_list3.sort()
my_list4.sort()
print(my_list3)  # ['a', 'b', 'g', 'g', 'h', 'h', 'r', 'v', 'w', 'y']
print(my_list4)  # [2, 5.3, 8, 14, 15, 49, 55, 233]
# NOTE above: You cannot sort a mixed objects list

# Nesting Lists
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]
matrix = [lst_1, lst_2, lst_3]
print(matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][2])  # 3

# List Comprehensions - Quick Construction of Lists
first_column = [row[0] for row in matrix] # Creates the first column of matrix
print(first_column)  # [1, 4, 7]




