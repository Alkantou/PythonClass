my_dogs = 2
print('My dogs are')
print(my_dogs + my_dogs + 7)

print(type(my_dogs))
print(len('Hello'))
# Sting Indexing
s: str = "Hello Vafouskos"
print(s[6]+s[7], s[9])
print(s[1:])
print(s[:7])
print(s[1:7], s[8:10])
print(s[-1], s[:-1], s[::-1], s[::3])

# String Properties. Immutability

# s[0] = 'X'  This command won't run because : TypeError: 'str' object does not
# support item assignment

# CONCATENATION : You are able to concatenate a string with a string
print(s[:-1], "stupid")  # Hello Vafousko stupid
print(s[0]*2 + s[1]*2)  # This prints "HHee"
print(s.upper()[::-1])  # No Error
print('Vafouskos'.upper()[::-1])  # No Error
print('Alex is the best'.split())  # Makes a list divided by blanks
print('Alex is the best'.split('e'))  # Makes a list divided by e but is are
# excluded : ['Al', 'x is th', ' b', 'st']
