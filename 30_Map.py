lst = ['a', 'b', 'c']
indext = []
lettert = []
for index, letter in enumerate(lst):
    indext.append(index)
    lettert.append(letter)
print(indext, lettert)

print(list(map(lambda x: (x*2) + '  %s' % x+x+x, lst)))
from functools import reduce
lst =[47,11,42,13]
if reduce(lambda x,y: x+y,lst) > 50:
    print(True)
else:
    print(False)