BOOK_PATH = "./books/frankenstein.txt"


def count_words(text):
    words = text.split()
    return len(words)

def get_file(path):
    with open(BOOK_PATH) as f:
        return f.read()

def main():
        book = get_file(BOOK_PATH)
        print(book)
        print(count_words(book))

main()