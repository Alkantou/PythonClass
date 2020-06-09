# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd


def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)


print(lesser_of_two_evens(5, 6))
print(lesser_of_two_evens(4, 2))


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        print('Nothing')


def master_yoda(sentence):
    return " ".join(sentence.split()[::-1])


def almost_there(num):
    return (abs(100 - num) in range(0, 11)) or (abs(200 - num) in range(0, 11))


# Right : We want all the list to be checked that's why else: goes under for and
# not under if

def has_332(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    else:  # # # # # # # # # # #
        return False


def paper_doll(text):
    char = ""
    for i in text:
        char += 3 * i
    return char


def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) > 21 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'Bust'


def summer_69(arr):
    total = 0
    switch = True
    for i in arr:
        while switch:
            if i != 6:
                total += i
                break
            else:
                switch = False
            while not switch:
                if i != 9:
                    break
                else:
                    switch = True
                    break
    return total


# SPY GAME : Write a function that takes in a list of integers and returns True if
# it contains 007 in order¶


def spy_game(arr):
    test_matrix = [0, 0, 7, 'x']

    for i in arr:
        if i == test_matrix[0]:
            test_matrix.pop(0)
    if len(test_matrix) == 1:
        return True
    else:
        return False


def spy_game_tutorial(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1

# COUNT PRIMES


