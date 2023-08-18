"""
Змініть функцію even_odd_generator так, щоб вона генерувала
послідовність чисел від 1 до n з рядками "Fizz" для чисел,
які діляться на 3, "Buzz" для чисел, які діляться на 5,
і "FizzBuzz" для чисел, які діляться як на 3, так і на 5.
"""


def even_odd_generator(num):
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            yield f"{i} - FizzBuzz"
        elif i % 3 == 0:
            yield f"{i} - Fizz"
        elif i % 5 == 0:
            yield f"{i} - Buzz"


my_generator = even_odd_generator(100)

for n in my_generator:
    print(n)
