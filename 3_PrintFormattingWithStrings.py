player = 'Thomas'
points = 33
print('Last night, ' + player + ' scored ' + str(points+5) + ' points.')
# If I wrote without the str() I would get error because String doesn't
# concatenate with integer(default class of numbers).
# Printing results in: Last night Thomas scored 38 points.
print(f'Last night, {player} scored {points + 2} points.')
# Printing results in: Last night Thomas scored 35 points.
print("I'm going to inject %s here." % 'Vafouskos')  # Parenthesis on Vafouskos is not needed
print("I'm going to inject %s here." % ('Vafouskos'))  #  Remove redundant parenthesis
print("I'm going to inject %s here and %s here." % ('Vafouskos', 'Vafouskitos'))
x, y, z = 'Alex', 'is', 'the best'
print('%s %s %r' % (x, y, z))  # Alex is the best
print('He said his name was %s.' % 'Vafouskos')
print('He said his name was %r.' % 'Vafouskos The Great')  # Difference between %s and %r
print('I once caught a fish %s.' %'this \tbig')  # \t inserts Tab : I once caught a fish this 	big.

