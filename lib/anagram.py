class Anagram:
    def __init__(self, word = ''):
        self.word = word

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):
        self._word = word

    def match(self, list_of_words = []):
        key_list = sorted([letter for letter in self.word])

        match_list = []

        i = 0
        while i < len(list_of_words):
            list_of_words[i] = [letter for letter in list_of_words[i]]
            if sorted(list_of_words[i]) == key_list:
                word_match = ''
                for letter in list_of_words[i]:
                    word_match += letter
                match_list.append(word_match)
            i += 1

        return match_list

