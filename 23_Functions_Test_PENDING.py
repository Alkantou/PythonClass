# Write a Python function that accepts a string and calculates the number of upper case
# letters and lower case letters.

def run_check(string):
    uppercount = 0
    lowercount = 0
    for word in string.split():
        for letter in word:
            if letter.isupper():
                uppercount += 1
            else:
                lowercount += 1
    print(lowercount, uppercount)

run_check('Alex is the BESt!')
# Same problem tutor's solution.
# def up_low(s):
#     d={"upper":0, "lower":0}
#     for c in s:
#         if c.isupper():
#             d["upper"]+=1
#         elif c.islower():
#             d["lower"]+=1
#         else:
#             pass
#     print("Original String : ", s)
#     print("No. of Upper case characters : ", d["upper"])
#     print("No. of Lower case Characters : ", d["lower"])


# Write a Python function that takes a list and returns
# a new list with unique elements of the first list.

def unique_elements(lst):
    return set(lst)

print(list(unique_elements([1, 5, 4, 5, 6, 4, 1])))
