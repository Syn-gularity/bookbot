def count_words(book):
    word_list = book.split()
    word_count = len(word_list)
    return word_count

def count_chars(book):
    lower_book = book.lower()
    char_list = list(lower_book)
    char_dict = {}
    for character in char_list:
        if character in char_dict:
            char_dict[character] = char_dict[character] + 1
        else:
            char_dict[character] = 1
    
    return char_dict

def sort_on(dict):
    return dict["amount"]

def sort_dict(char_dict):
    char_dict_list = []
    for char in char_dict:
        new_dict = {"char": char, "amount": char_dict[char]}
        char_dict_list.append(new_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list