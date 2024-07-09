class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Convert the tuple to a list

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for i, string in enumerate(file):
                    low_line = string.lower()
                    for char in low_line:
                        if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            low_line = low_line.replace(char, '')
                            words = low_line.split()
                            all_words[i, file_name] = words

        return all_words



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
