"""
Напишіть генератор, який видає послідовність простих чисел.
"""


class PalindromeIterator:
    def __init__(self, word_list):
        self.end_point = 0
        self.word_list = word_list

    def __iter__(self):
        return self

    def __next__(self):
        while self.end_point < len(self.word_list):
            word = self.word_list[self.end_point]
            self.end_point += 1
            if word == word[::-1]:
                return word
        raise StopIteration


word_list = ["level", "racecar", "python", "madam"]
palindrome_iter = PalindromeIterator(word_list)
for word in palindrome_iter:
    print(word)







