# Tuples are like Lists but IMMUTABLE: they cannot be changed

t = (1, 2, 3)
print(len(t))  # Prints 3
t = ('one', 2, 4, 4)
print(t)  # Prints ('one', 2)
print(t[0])  # Prints 1

# Basic Tuple Methods
print(t.index('one'))  # Prints the index of 'one': 0
print(t.count(4))  # Counts the number of times 4 appears in the tuple: 1

# t[0] = 'one' or t.append('nope') are not functioning because tuples are immutable
