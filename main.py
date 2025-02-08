BOOK_PATH = "./books/frankenstein.txt"

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
        print(book)
        print(count_words(book))
        char_freq = get_char_freq(book)
        print(char_freq)

main()