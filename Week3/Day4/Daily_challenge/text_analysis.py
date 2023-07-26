import re
from collections import Counter
from operator import itemgetter

class Text:
    def __init__(self, text='A good book would sometimes cost as much as a good house.'):
        self.text = text
        self.wordsDict = self.calculate_frequency()

    def calculate_frequency(self):
        words_list = re.split(r'[^a-zA-Z]+', self.text.lower())
        words_list.remove('')
        return Counter(words_list)

    def most_common_words(self):
        max_frequency = max(self.wordsDict.values())
        most_common_list = list(filter(lambda item: item[1] == max_frequency, self.wordsDict.items()))
        return list(map(itemgetter(0), most_common_list))
        # return [word for word, count in self.wordsDict.items() if count == max_frequency]

    def unique_words(self):
        return [word for word, count in self.wordsDict.items() if count == 1]

    @classmethod
    def from_file(cls, name_file):
        with open(name_file, "r") as file:
            lines = file.readlines()
            text = ' '.join(lines)
            return cls(text)   

# text_analysis = Text()
text_analysis = Text.from_file('the_stranger.txt')
print(text_analysis.most_common_words())
print(text_analysis.unique_words())        