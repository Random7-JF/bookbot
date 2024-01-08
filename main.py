def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(get_word_count(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(book:str):
    words = book.split(" ")
    return len(words)


main()