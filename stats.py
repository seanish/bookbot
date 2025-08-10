
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
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters.update({char: 1})
    return characters

def create_list(characters):
    list_of_dict = list()
    for char in characters:
        list_of_dict.append({"char": char, "num": characters[char]})
    return list_of_dict

def sort_on(items):
    return items["num"]

def create_final_count(book):
    characters = count_characters(book)
    list = create_list(characters)
    list.sort(reverse=True, key=sort_on)
    return list
