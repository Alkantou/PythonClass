class MyString:

    def __init__(self, word):
        self.word = list(word)

    def capitalize(self):
        self.word[0] = self.word[0].upper()
        return ''.join(self.word)