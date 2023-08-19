"""
Напишіть генератор, який фільтрує непарні числа з заданої послідовності.
"""


def even_number_filter(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
even_nums = even_number_filter(numbers)
for num in even_nums:
    print(num)

