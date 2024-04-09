def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_words(book_text)
    letter_count = get_letters(book_text)
    print(letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    character_count = {}
    for c in text:    
        c_lowered = c.lower()
        if c_lowered in character_count:
            character_count[c_lowered] += 1
        else:
            character_count[c_lowered] = 1
    return character_count

main()
