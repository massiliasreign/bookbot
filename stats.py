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
        letter = letter.lower()
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    
    print(letter_counts)