
def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def count_words(book):
    text = get_book_text(book)
    words = text.split()
    return len(words)

def count_characters(book):
    text = get_book_text(book)
    characters = {}
    for char in text:
        char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters.update({char: 1})
    return characters
