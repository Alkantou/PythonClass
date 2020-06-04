
import random
# from random import randint
#
# five = [randint(0, 41) for x in range(0, 6)]
# print(five)

for _ in range(0, 4):
    x = random.sample(range(1, 46), 5)
    j = random.sample(range(1, 21), 1)

    print(f'X={x}')
    print(f'Joker={j}')

# for i in range(1, 46):
#     print(i)