from stats import count_characters, count_words

def main():
    word_count = count_words("books/frankenstein.txt")
    character_count = count_characters("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(character_count)

main()
