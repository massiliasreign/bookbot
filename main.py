import sys
from stats import get_num_words, sorted_letter_count
def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars = sorted_letter_count(text)
    for item in chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()