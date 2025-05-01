import sys
from stats import get_num_words
from stats import count_char
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = f"{sys.argv[1]}"
    book_text = get_book_text(filepath)
    # print(book_text)
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")
    dictionary = count_char(book_text)
    sorted = sort_dict(dictionary)
    for item in sorted:
        print(f"{item['char']}: {item['num']}")
    
main()