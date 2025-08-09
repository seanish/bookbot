from stats import count_words

def main():
    word_count = count_words("books/frankenstein.txt")
    print(f"{word_count} words found in the document")

main()
