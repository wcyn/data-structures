# https://www.interviewcake.com/question/python/word-cloud?course=fc1&section=hashing-and-hash-tables
# Write code that takes a long string and builds its word cloud data in a dictionary,
# where the keys are words and the values are the number of times the words occurred.


class WordCloud:
    word_map = {}

    def __init__(self, words=''):
        self.words = words

    def split_words(self):

        word_start,  word_length = 0, 0
        print(len(self.words))
        for index, char in enumerate(self.words):
            if not char.isalpha():
                if char in {"-", "'"}:
                    word_length += 1
                    continue
                if word_length > 0:
                    word_string = self.words[word_start: word_start + word_length]
                    self.add_word_to_map(word_string)
                word_start = index + 1
                word_length = 0  # reset

            else:
                word_length += 1
                if index == len(self.words) - 1:
                    word_string = self.words[word_start: word_start + word_length + 1]
                    self.add_word_to_map(word_string)
        print(id(self.word_map))
        return self.word_map

    def add_word_to_map(self, word):
        if word in self.word_map:
            self.word_map[word] += 1
        else:
            lower_word = word.lower()
            upper_word = word.title()
            if lower_word in self.word_map:
                self.word_map[lower_word] += 1
            elif upper_word in self.word_map:
                self.word_map[lower_word] = 1
                self.word_map[lower_word] += self.word_map[upper_word]
                del self.word_map[upper_word]
            else:
                self.word_map[word] = 1


words2 = "Friends, Romans, countrymen! today Let us eat cake. Romans stay up-stay  it's romans Romans  " \
         " stay   st I'm singing ♬ on a ☔ day."
print(WordCloud(words2).split_words())
