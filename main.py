import sys
from stats import get_num_words
from stats import get_chars_dict
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
