
def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    characters_dictionary = {}
    for char in text.lower():
        if char in characters_dictionary:
            characters_dictionary[char] += 1
        else:
            characters_dictionary[char] = 1
    return characters_dictionary


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list