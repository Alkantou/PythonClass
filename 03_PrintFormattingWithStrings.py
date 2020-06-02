player = 'Thomas'
points = 33
print('Last night, ' + player + ' scored ' + str(points+5) + ' points.')
# If I wrote without the str() I would get error because String doesn't
# concatenate with integer(default class of numbers).
# Printing results in: Last night Thomas scored 38 points.
print(f'Last night, {player} scored {points + 2} points.')
# Printing results in: Last night Thomas scored 35 points.
print("I'm going to inject %s here." % 'Vafouskos')  # Parenthesis on Vafouskos is not needed
print("I'm going to inject %s here." % ('Vafouskos'))  # Remove redundant parenthesis
print("I'm going to inject %s here and %s here." % ('Vafouskos', 'Vafouskitos'))
x, y, z = 'Alex', 'is', 'the best'
print('%s %s %r' % (x, y, z))  # Alex is the best
print('He said his name was %s.' % 'Vafouskos')
print('He said his name was %r.' % 'Vafouskos The Great')  # Difference between %s and %r
print('I once caught a fish %s.' % 'this \t\tbig')  # \t inserts 2Tab : I once caught a fish this 	big.
# BUT in case I use %r I get I once caught a fish 'this \tbig'
print('I wrote %s programs today.' % 3.75)  # Prints 3.75
print('I wrote %d programs today.' % 3.75)  # Prints 3
# NOTE: The %s operator converts whatever it sees into a string, including integers and floats.
# The %d operator converts numbers to integers first, without rounding. Note the difference above:

# Padding and Precision of Floating Point Numbers. #

# Skipped This part for Now.#


# Multiple Formatting.
print('First: %s, Second: %5.2f, Third: %r' % ('hi!', 3.1415, 'bye!'))
# Prints: First: hi!, Second:  3.14, Third: 'bye!'

# FORMATTING WITH THE .format() method.#
print('This is a string with an {}'.format('insert'))
print('I am Alexandros {}'.format('Kantounis'))
#  Inserted Objects can be called by index position.
print("{1} {0} {2}".format('is', 'Vafouskos', 'Stupid'))
# Assigned key words
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1, b='Two', c=12.3))
# Unlike %s inserted objects can be reused
print('A {p} saved is a {p} earned.'.format(p='penny'))
# Instead of print('A %s saved is a %s earned.' %('penny','penny'))
