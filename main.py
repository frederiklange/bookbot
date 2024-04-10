# Defining main function to be called
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_words(book_text)
    letter_count = get_letters(book_text)
    letter_count_sorted = sort_dict(letter_count)
    print_report(book_path, word_count, letter_count_sorted)
    
# Opens a text file from a path with a book
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Function that splits a text into a list of words and return the number of words in the text
def get_words(text):
    words = text.split()
    return len(words)

# Function that get the letters from a text and add them to a dictionary with count as value
def get_letters(text):
    character_count = {}
    for c in text:    
        c_lowered = c.lower()
        in_alpha = c_lowered.isalpha()
        if in_alpha == False:
            continue
        elif c_lowered in character_count:
            character_count[c_lowered] += 1
        else :
            character_count[c_lowered] = 1
    return character_count

# Function to sort the dictionary of letters with counts
def sort_dict(letter_dict):
    sorted_dict = sorted(letter_dict.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_dict)

# Function to print the final report
def print_report(book_path, word_count, letter_count_sorted):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for k in letter_count_sorted:
        print(f"The '{k}' character was found {letter_count_sorted[k]} times")
    
    print("--- End report ---")

# Calling main function to print book report
main()
