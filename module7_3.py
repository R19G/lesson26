class WordsFinder:

    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        d = ''
        all_words = {}
        punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, 'r', encoding='utf-8') as f:
            for i in f:
                i = i.lower()
                for j in i:
                    if j in punctuations:
                        i = i.replace(i, '')
                d = d + i
            all_words.update({self.file_names: d.split()})
        return all_words

    def find(self, txt):
        dist = {}
        word = self.get_all_words()[self.file_names]
        for i in range(len(word)):
            if txt.lower() == word[i]:
                dist.update({self.file_names: i+1})
                return dist

    def count(self, txt):
        dist = {}
        world = self.get_all_words()[self.file_names]
        dist.update({self.file_names: world.count(txt.lower())})
        return dist


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
