from stats import get_num_words, sorted_letter_count 
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
get_num_words()
print("--------- Character Count -------")
chars = sorted_letter_count()
for item in chars:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")