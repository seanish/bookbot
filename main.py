from stats import count_words, create_final_count

def main():
    word_count = count_words("books/frankenstein.txt")
    character_count = create_final_count("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    i = 0
    while i < len(character_count) - 1:
        i += 1
        if character_count[i]["char"].isalpha() != True:
            continue
        else:
            print(f"{character_count[i]['char']}" ": " f"{character_count[i]['num']}")

    print("============= END ===============")

main()
