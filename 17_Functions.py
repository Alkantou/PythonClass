

def say_hello():

    print("hello bafitos!")


say_hello()
say_hello()
say_hello()


def greeting(name):
    print('Hello %s' % name)


greeting('Vafouskos')


def multiply(n1, n2, n3):
    return n1*n2*n3


print(multiply(1, 2, 4))
# print(multiply('Alex', "Baf", "Elena"))  # Error: No Multiply between strings only +


def is_prime(num):

    # Naive method of checking for primes.

    for n in range(2, num):
        if num % n == 0:
            print(num, 'is not prime')
            break
    else:  # If never mod zero, then prime
        print(num, 'is prime!')



is_prime(50)


import math   # Normally always at the top of the file.


def is_prime2(num):  # Better Method
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
