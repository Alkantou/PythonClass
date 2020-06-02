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

