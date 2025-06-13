from stats import count_words
from stats import count_chars
from stats import sort_dict
import sys

def get_book_text(filepath):
    text = None
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    book = get_book_text(book_path)
    num_words = count_words(book)
    print(f"Found {num_words} total words")
    char_dict = count_chars(book)
    list_char_dict = sort_dict(char_dict)
    print("--------- Character Count -------")
    for dicti in list_char_dict:
        if dicti["char"].isalpha():
            print(f"{dicti["char"]}: {dicti["amount"]}")
    print("============= END ===============")


main()
