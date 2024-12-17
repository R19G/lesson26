class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):

        all_words = dict()
        list_of_punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']
        list_of_strings = []
        for file in self.file_names:
            with open(file, encoding='utf-8') as f_number:
                for i in f_number:
                    i = i.lower()
                    for symbol in list_of_punctuations:
                        i = i.replace(symbol, '' if symbol != ' - ' else ' ')
                    list_of_strings.extend(i.split())
                all_words[file] = list_of_strings
                list_of_strings = []
        return all_words

    def find(self, word):
        word = word.lower()
        dictionary_1 = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                dictionary_1[file_name] = words.index(word) + 1
        return dictionary_1

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) 
print(finder2.find('TEXT')) 
print(finder2.count('teXT')) 
