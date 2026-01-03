def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def get_num_words():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text = text.split()
    num_words = len(text)
    print(f"Found {num_words} total words")
def letter_count():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_counts = {}
    for letter in text:
        if not letter.isalpha():
            continue
        letter = letter.lower()
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    
    print(letter_counts)
    return letter_counts
def sorted_letter_count():
    letter_counts = letter_count()
    # sort the dictionary from greatest to least by value
    sorted_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    print(sorted_counts)