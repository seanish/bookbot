
def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def count_words(book):
    text = get_book_text(book)
    words = text.split()
    return len(words)
