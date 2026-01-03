import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
from stats import get_num_words, sorted_letter_count 
print("============ BOOKBOT ============")
print("Analyzing book found at books/...")
print("----------- Word Count ----------")
get_num_words()
print("--------- Character Count -------")
chars = sorted_letter_count()
for item in chars:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")