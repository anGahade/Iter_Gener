"""
Створіть ітератор який буде приймати рядок та кожен виклик методу next()
буде повертати наступний символ рядку.
"""


class NextLetter:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.string):
            result = self.string[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


string = "Hello, world!"
str_itr = NextLetter(string)
for char in string:
    print(char)
