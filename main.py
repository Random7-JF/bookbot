def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(book)} words found in the document")
    letters = get_letter_count(book)
    stats = get_letter_stats(letters)
    for stat in stats:
        print_stat(stat[0], stat[1])

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

def get_letter_stats(letters:dict) -> list:
    letter_list = []
    for letter in letters:
        if letter.isalpha():
            letter_list.append((letter, letters[letter]))
    
    # Sort the list in place -- ty boots.
    letter_list.sort(key=lambda x: x[1], reverse=True)  # sorts by the second item of the tuple in descending order
    return letter_list

def print_stat(letter:str, value:int):
    print(f"The '{letter}' character was found {value} time(s)")

main()