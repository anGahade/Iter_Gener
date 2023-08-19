"""
Напишіть генератор, який фільтрує непарні числа з заданої послідовності.
"""


class EvenRangeIterator:
    def __init__(self, a, b):
        self.current = a + (a % 2)
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.b:
            num = self.current
            self.current += 2
            return num

        raise StopIteration


even_nums = EvenRangeIterator(1, 10)
for num in even_nums:
    print(num)

