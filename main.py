from stats import get_num_words
from stats import count_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    print(book_text)
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")
    dictionary = count_char(book_text)
    print(dictionary)
    
    
main()