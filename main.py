import sys
from stats import get_num_words, get_char_count, sort_dictionary

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    chars_sorted_list = sort_dictionary(char_count)
    print_report(book_path, word_count, chars_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, word_count, chars_sorted_list):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()