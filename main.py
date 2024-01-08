def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(get_word_count(text))
    letters = get_letter_count(text)
    print(letters)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(book:str):
    words = book.split()
    return len(words)

def get_letter_count(book:str) -> dict:
    letterstats = dict()
    for letter in book.lower():
        if letter not in letterstats.keys():
            letterstats[letter] = 1
        else:
            letterstats[letter] = letterstats[letter] +1
    return letterstats


main()