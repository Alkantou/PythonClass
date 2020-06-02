list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd numba!')
list_sum = 0
list1.reverse()
for num in list1:  # Question for Vafouskos?
    list_sum += num
print(list_sum)
print(list1)

for letter in 'Vafouskos is stupid!':
    print(letter*2)

# Special Quality of Tuples in iteration. UNPACKING
list2 = [(2, 4), (6, 8), (10, 12)]
for tup in list2:
    print(tup)

for (t1, t2) in list2:
    print(t1)

# Dictionaries
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
for k,v in d.items():
    print(k)
    print(v)