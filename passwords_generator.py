import random
import nltk

APPEARING_TIME = 1
NUMBER_OF_MIX = 32

class SaferPasswordsGenerator:
    
    def __init__(self):
        # Download the list of English words from the NLTK library
        nltk.download('words')

        # Get the list of words
        self.word_list = nltk.corpus.words.words()

        # Create a Counter to store the number of times each word appears
        word_counts = nltk.Counter(self.word_list)

        # Create a list of words that appear more than APPEARING_TIME times
        filtered_words = []
        for word, count in word_counts.items():
            if count > APPEARING_TIME:
                filtered_words.append(word)

        self.word_list = filtered_words
        

    def mix_list(self, numbers_of_shuffle: int = NUMBER_OF_MIX):
        """Mixes the elements of a list in random order."""

        for _ in range(numbers_of_shuffle):

            random.shuffle(self.word_list)

    def get_random_str_with_special_char_and_case(self, uppercase: bool,number_of_elements: int, spec_char = ' '):
        lst = self.__get_random_elements(number_of_elements)

        if uppercase:
            lst = self.__words_to_uppercase(lst)

        return self.__build_string_words_and_special_char(lst, spec_char)


    def __get_random_elements(self, number_of_elements: int) -> list:
        """Gets n random elements from a list."""

        return self.word_list[:number_of_elements]
    
    
    def __build_string_words_and_special_char(self, words_lst: list, spec_char = ' '):

        # return string, where each word sperated with spec_char
        return (spec_char.join(words_lst))
    
    def __words_to_uppercase(self, lst: list):
        lst_uppercase = []
        for word in lst:
            lst_uppercase.append(word[0].upper() + word[1:])
        
        return lst_uppercase
    

    def filter_words_by_length(self, min_len_word: int, max_len_word: int):
        words_list_filtered = list()

        for word in self.word_list:
            word_len = len(word)

            if word_len >= min_len_word and word_len <= max_len_word:
                words_list_filtered.append(word)

        self.word_list = words_list_filtered


    def add_numbers_to_pass(self, password: str) -> str:

        char_num = len(password)
        password += str(char_num)
        return password
    

    

    

