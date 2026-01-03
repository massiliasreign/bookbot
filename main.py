#def get_book_text(filepath):
   # with open(filepath) as f:
  #      file_contents = f.read()
 #       return file_contents
#def main():
   # book_path = "books/frankenstein.txt"
  #  text = get_book_text(book_path)
 #   print(text)
#main()
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text = text.split()
    num_words = len(text)
    print(f"Found {num_words} total words")
main()