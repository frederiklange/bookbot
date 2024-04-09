def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_words(book_text)
    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

main()
