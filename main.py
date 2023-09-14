import passwords_generator

lst_special_chars = ['!', '#', '$', '%', '^', '&', '*', '+', '=', '-', '_', '<', '>', ',' , '.', '?', ':']

def main():

    min_len = int(input("Please enter the minimum length of each word (recommended is 3): "))
    max_len = int(input("Please enter the maximum length of each word (recommended is 7): "))

    num_of_words = int(input("Please enter the numbers of word you want to receive: "))

    special_char = input("If you want to separate the words with a special character please type it, otherwise type n: ")
    if not special_char in lst_special_chars:
        print("The special character is not in the list, we replace is with space")
        special_char = ' '


    upper_case = input('Do you want all the words with upper case? (y/n): ').lower().strip() == 'y'

    

    pas_gen1 = passwords_generator.SaferPasswordsGenerator()

    pas_gen1.filter_words_by_length(min_len, max_len)
    pas_gen1.mix_list()
    random_elements = pas_gen1.get_random_str_with_special_char_and_case(upper_case, num_of_words, special_char)
    random_elements = pas_gen1.add_numbers_to_pass(random_elements)
    print("Random elements:", random_elements)

    write_to_file = input("Do you want to save the password to a file? (y/n): ")
    
    while write_to_file != 'y' and write_to_file != 'n':
        write_to_file = input("Wrong input! Do you want to save the password to a file? (y/n): ")

    if write_to_file == 'y':
        print('yes')
    elif write_to_file == 'n':
        print('no')
    

if __name__ == '__main__':
    main()

