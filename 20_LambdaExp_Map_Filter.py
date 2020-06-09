# Map FUNCTION
def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]


mynames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']

# for i in mynames:
#     if len(i) % 2 == 0:
#         print('even')
#     else:
#         print(i[0])

print(list(map(splicer, mynames)))


# Filter Function
def check_even(num):
    return num % 2 == 0


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(check_even, nums)))

# Lambda Expression

list(map(lambda num: num ** 2, my_nums))
list(filter(lambda n: n % 2 == 0,nums))


