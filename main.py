"""
Напишіть генератор, який повертає послідовність чисел Фібоначчі.
"""


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


my_fibonacci_generator = fibonacci_generator()

for n in range(21):
    print(next(my_fibonacci_generator))
