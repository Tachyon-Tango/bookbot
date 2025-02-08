BOOK_PATH = "books/frankenstein.txt"

def sort_key(dict):
    return dict["num"]

def convert_dict(dict):
    list_of_dict = []
    for key in dict:
        if key.isalpha():
            temp_dict = {"char" : key, "num" : dict[key]}
            list_of_dict.append(temp_dict)
    return list_of_dict

def get_file(path):
    with open(BOOK_PATH) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_char_freq(text):
    result_dict = {}
    for char in text.lower():
        if char in result_dict:
            result_dict[char] = result_dict[char] + 1
        else:
            result_dict[char] = 1
    return result_dict


def main():
        book = get_file(BOOK_PATH)
        word_count = count_words(book)
        char_freq = get_char_freq(book)
        conv_char_freq = convert_dict(char_freq)
        conv_char_freq.sort(reverse=True, key=sort_key)

        print(f"--- Begin report of {BOOK_PATH} ---")
        print(f"{word_count} words found in the document")
        print("")
        for element in conv_char_freq:
            char = element["char"]
            num = element["num"]
            print(f"The '{char}' character was found {num} times")
        print("--- End report ---")


main()