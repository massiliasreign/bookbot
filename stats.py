def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words
def letter_count(text):
    letter_counts = {}
    for letter in text:
        if not letter.isalpha():
            continue
        letter = letter.lower()
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    
    return letter_counts

def sort_on(item):
    return item["num"]

def sorted_letter_count(text):
    letter_counts = letter_count(text)
    sorted_list = []

    for char, count in letter_counts.items():
        sorted_list.append({
            "char": char,
            "num": count
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
