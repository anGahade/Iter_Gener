"""
Напишіть генератор, який видає послідовність простих чисел.
"""


def isprime(n):
    if n == 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def prime_generator(n=2):
    while True:
        if isprime(n):
            yield n
        n += 1


prime_gen = prime_generator()
for i in range(10):
    print(next(prime_gen))



