"""
Реалізуйте ітератор для перебору всіх ключів словника.
"""


class DictKeyIterator:
    def __init__(self, dictionary):
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            self.index += 1
            return key
        else:
            raise StopIteration


my_dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeyIterator(my_dictionary)
for key in dict_iter:
    print(key)
