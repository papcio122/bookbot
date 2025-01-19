def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    characters_dictionary = {}
    for char in text.lower():
        if char in characters_dictionary:
            characters_dictionary[char] += 1
        else:
            characters_dictionary[char] = 1
    return characters_dictionary


main()
