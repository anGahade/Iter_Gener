"""
Напишіть генератор, який видає послідовність квадратів чисел від 1 до N.
"""


def square_generator(n):
    for x in range(1, n+1):
        yield x**2


for g in square_generator(5):
    print(g)
