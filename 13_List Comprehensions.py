# List comprehensions allow us to build out lists using a different notation.
# You can think of it as essentially a one line for loop built inside of brackets.
# For a simple example:

# Grab every letter in string
lst = [x for x in 'Vafouskos']
print(lst)  # ['V', 'a', 'f', 'o', 'u', 's', 'k', 'o', 's']
# You can replace anything
lst = [['Baf', 5] for x in ['a', 'b']]
print(lst)  # [['Baf', 5], ['Baf', 5]]

lst = [x for x in range(11) if x % 2 == 0]
print(lst)  # [0, 2, 4, 6, 8, 10]

list = [1, 2, 3, 4, 5, 6, 7, 8]
a_third_of_a_square_list = [x ** 2 / 3 for x in list]
print(a_third_of_a_square_list)

# Nested list comprehensions
lst = [x*3 for x in [x**2 for x in [1, 7]]]
print(lst)  # [3, 147]
